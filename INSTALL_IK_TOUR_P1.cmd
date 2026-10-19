@echo off
setlocal
pushd "%~dp0"
where python >nul 2>&1
if not errorlevel 1 (
  python "tools\tandem_tour\installer.py" install --repo "%CD%"
) else (
  py -3 "tools\tandem_tour\installer.py" install --repo "%CD%"
)
set "rc=%errorlevel%"
popd
pause
exit /b %rc%
