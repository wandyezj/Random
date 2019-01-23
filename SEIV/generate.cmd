@ECHO OFF
PUSHD %~dp0
ECHO %CD%

REM DIR /B *.py

:: generated components
FOR /F %%i IN ('DIR /B *.py') DO (
    python.exe %%i
)

:: manually created components
FOR /F %%i IN ('DIR /B *.txt') DO (
    COPY %%i .\mod_snips\%%i > NUL
)

POPD