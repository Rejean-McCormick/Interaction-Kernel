"""Offline hash-pinned Tandem 4/8 installer; no service/database/network calls."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

SCRIPT = Path(__file__).resolve()
BUNDLE = SCRIPT.parents[2]
MANIFEST = json.loads((SCRIPT.parent / 'manifest.json').read_text(encoding='utf-8'))
FILES = MANIFEST['files']


def sha(path: Path) -> str | None:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def valid_repo(repo: Path) -> None:
    if not (repo/'contracts/profiles/index.json').is_file() or not (repo/'runtime/python/src/interaction_kernel/profile_registry.py').is_file():
        raise ValueError(f'Invalid IK repository root: {repo}')
    if (repo/'tools/tandem_tour/installer.py').resolve() != SCRIPT:
        raise ValueError('The installer must be placed at the IK repository root')


def inspect(repo: Path) -> dict[str, str]:
    if MANIFEST.get('format') != 'ik.tandem-tour-update/1':
        raise ValueError('Invalid pack manifest')
    paths = [entry['path'] for entry in FILES]
    if len(paths) != len(set(paths)):
        raise ValueError('Duplicate payload file')
    state = {}
    for e in FILES:
        rel = Path(e['path'])
        target=(repo/rel).resolve(); payload=(SCRIPT.parent/'payload'/rel).resolve()
        if not target.is_relative_to(repo.resolve()) or not payload.is_relative_to((SCRIPT.parent/'payload').resolve()):
            raise ValueError(f'Unsafe payload path: {rel}')
        if sha(payload)!=e['updated_sha256']:
            raise ValueError(f'Package integrity failed: {rel}')
        actual=sha(target)
        if actual==e['updated_sha256']:
            state[e['path']]='ALREADY_UPDATED'
        elif actual==e['original_sha256']:
            state[e['path']]='READY'
        else:
            raise ValueError(f'Local file diverged; refusing overwrite: {rel}')
        print(f'[{state[e["path"]]}] {rel.as_posix()}')
    return state


def run(cmd: list[str], cwd: Path, env: dict[str, str] | None = None) -> None:
    print('[TEST] '+' '.join(cmd), flush=True)
    subprocess.run(cmd,cwd=cwd,env=env,check=True,timeout=120)


def test_stage(repo: Path, state: dict[str, str]) -> None:
    # No writes to the installed repository; compile and test an isolated tree.
    with tempfile.TemporaryDirectory(prefix='ik-tour4-check-') as tmp:
        stage=Path(tmp)/'repo'
        def ignored(_dir, names):
            return {name for name in names if name in {'.git','node_modules','dist','__pycache__','.venv','venv','.env','.env.local','Tandem_Local'}}
        shutil.copytree(repo,stage,ignore=ignored)
        for e in FILES:
            rel=Path(e['path'])
            dest=stage/rel
            dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(SCRIPT.parent/'payload'/rel,dest)
        run([sys.executable,'-m','compileall','-q',str(stage/'runtime/python/src/interaction_kernel'),str(stage/'scripts'),str(stage/'runtime/python/tests')],stage)
        run([sys.executable,'scripts/verify_tandem_contract_lock.py'],stage)
        env=os.environ.copy();env['PYTHONPATH']=str(stage/'runtime/python/src')
        try:
            import jsonschema  # type: ignore[import-untyped]
        except ImportError:
            print('[ATTENTE] jsonschema absent: tests Python complets non executes, aucun paquet installe')
        else:
            run([sys.executable,'scripts/validate_repo.py'],stage,env)
            run([sys.executable,'-m','unittest','discover','-s','runtime/python/tests','-q'],stage,env)
            run([sys.executable,'scripts/verify_kristal_lock.py'],stage)
            run([sys.executable,'scripts/verify_kristal_v7_baseline.py'],stage)
        node=shutil.which('node')
        if node:
            run([node,'runtime/typescript/test/tandem-contracts.mjs'],stage)
        else:
            print('[ATTENTE] Node.js absent: controles TypeScript non executes')
        tsc=shutil.which('tsc')
        if node and tsc:
            run([tsc,'-p','tsconfig.json'],stage/'runtime/typescript')
            run([node,'test/run-tests.mjs'],stage/'runtime/typescript')
            run([tsc,'--noEmit','--strict','--target','ES2023','--module','NodeNext','--moduleResolution','NodeNext','../../adapters/orgo-typescript/orgo-ik-adapter.ts','src/types.ts'],stage/'runtime/typescript')
        elif node:
            print('[ATTENTE] compilateur TypeScript absent: tests dist differes; test lock Node termine')


def backup_dir(repo: Path) -> Path:
    return repo.parent/'Tandem_Local'/'interaction_kernel_tour_p1'/'backups'


def install(repo: Path, state: dict[str, str]) -> None:
    if all(v=='ALREADY_UPDATED' for v in state.values()):
        print('[OK] Deja installe; aucune modification');return
    test_stage(repo,state)
    base=backup_dir(repo);base.mkdir(parents=True,exist_ok=True)
    suffix=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    current=base/suffix
    current.mkdir(parents=True,exist_ok=False)
    to_change=[e for e in FILES if state[e['path']]=='READY']
    info={'format':'ik-tour-backup/1','files':to_change}
    for e in to_change:
        rel=Path(e['path']); before=repo/rel
        if before.exists():
            target=current/'original'/rel;target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(before,target)
    (current/'backup.json').write_text(json.dumps(info,indent=2)+'\n',encoding='utf-8')
    try:
        for e in to_change:
            rel=Path(e['path']); source=SCRIPT.parent/'payload'/rel; target=repo/rel
            if sha(target)!=e['original_sha256']:
                raise ValueError(f'Concurrent modification detected: {rel}')
            target.parent.mkdir(parents=True,exist_ok=True)
            temp=target.with_name(target.name+'.ik-tour.tmp')
            try:
                shutil.copyfile(source,temp)
                os.replace(temp,target)
            finally:
                temp.unlink(missing_ok=True)
        inspect(repo)
    except Exception:
        for e in reversed(to_change):
            rel=Path(e['path']); original=current/'original'/rel; target=repo/rel
            if original.exists():
                target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(original,target)
            else: target.unlink(missing_ok=True)
        print('[ROLLBACK] Echec, sources initiales restaurees');raise
    print(f'[OK] Interaction Kernel Tour 4/8 installe. Sauvegarde: {current}')
    print('[INFO] Aucun IK en service, tenant, image Docker, VPS ou DB modifie')


def rollback(repo:Path) -> None:
    base=backup_dir(repo)
    backups=sorted(base.glob('*/backup.json')) if base.exists() else []
    if not backups: raise ValueError('Aucune sauvegarde disponible')
    manifest_path=backups[-1]; data=json.loads(manifest_path.read_text(encoding='utf-8')); backup=manifest_path.parent
    print(f'[BACKUP] {backup}')
    # Entire rollback is refused when any installed source was edited afterwards.
    for e in data['files']:
        if sha(repo/e['path'])!=e['updated_sha256']:
            raise ValueError(f'Local drift since installation, rollback refused: {e["path"]}')
    for e in data['files']:
        target=repo/e['path'];original=backup/'original'/e['path']
        if e['original_sha256'] is None:target.unlink()
        else:
            if sha(original)!=e['original_sha256']:
                raise ValueError(f'Corrupt backup: {e["path"]}')
            target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(original,target)
    manifest_path.rename(backup/'backup.rolled_back.json')
    print('[OK] Retour arriere termine; aucun deploiement effectue')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('action',choices=['preview','install','verify','rollback'])
    parser.add_argument('--repo',default=str(BUNDLE))
    args=parser.parse_args()
    repo=Path(args.repo).resolve();valid_repo(repo)
    print('=== IK / TANDEM / TOUR 4 SUR 8 / '+args.action.upper()+' ===')
    print(f'[REPO] {repo}')
    print('[PORTEE] Sources uniquement. Aucune connexion a un service externe ou DB.')
    if args.action=='rollback':rollback(repo);return
    state=inspect(repo)
    if args.action=='preview':print('[OK] Apercu favorable, lecture seule')
    elif args.action=='install':install(repo,state)
    else:
        if not all(s=='ALREADY_UPDATED' for s in state.values()):
            raise ValueError('Le correctif n\'est pas entierement installe')
        test_stage(repo,state)
        print('[OK] Fichiers conformes et tests disponibles passes')

if __name__=='__main__':
    try:main()
    except (ValueError,OSError,subprocess.SubprocessError) as exc:
        print(f'[BLOQUE] {exc}',file=sys.stderr);sys.exit(1)
