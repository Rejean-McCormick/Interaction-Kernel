// Read-only conformance: the active tandem contract set cannot silently drift.
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const readJSON = p => JSON.parse(fs.readFileSync(path.join(root, p), 'utf8'));
const lock = readJSON('contracts/locks/konnaxion-orgo-adopted-v1.lock.json');
const index = readJSON('contracts/profiles/index.json');
assert.equal(lock.format, 'ik.adopted-profile-lock/1');
assert.equal(lock.specversion, 'ik/1.1');
assert.equal(lock.scope, 'konnaxion-orgo');
const adopted = [
  ['governance.decision.execute','1.0.0','command'],
  ['accountability.impact.publish','1.0.0','command'],
  ['operational.reconsideration.recommended','1.0.0','event'],
];
const indexed = index.profiles.map(p => `${p.id}@${p.version}:${p.class}`);
assert.equal(new Set(indexed).size, indexed.length, 'duplicate profile in active index');
for (const [id,version,cl] of adopted) assert.ok(indexed.includes(`${id}@${version}:${cl}`), `${id} not active`);
const files = new Set();
for (const [id,version] of adopted) for (const filename of ['profile.json','payload.schema.json']) files.add(`contracts/profiles/konnaxion-orgo/${id}/${version}/${filename}`);
assert.equal(lock.files.length, files.size);
for (const entry of lock.files) {
  assert.ok(files.delete(entry.path), `unexpected or duplicate lock path ${entry.path}`);
  const actual = 'sha256:' + createHash('sha256').update(fs.readFileSync(path.join(root,entry.path))).digest('hex');
  assert.equal(actual, entry.sha256, `drift in ${entry.path}`);
}
assert.equal(files.size,0);
console.log('PASS adopted Konnaxion-Orgo profiles=3 immutable digests=6');
