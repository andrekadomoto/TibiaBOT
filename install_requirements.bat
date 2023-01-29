@echo off

set "VIRTUAL_VENV=venv"

IF EXIST %VIRTUAL_VENV%\Scripts\activate (
	goto :read_venv
) ELSE (
	py -m pip install --upgrade pip
	py -m pip --version
	py -m pip install --user virtualenv
	py -m venv venv
	CALL :read_venv
	EXIT
)

:read_venv
call venv\Scripts\activate.bat
start py -m pip install -r requirements.txt --src venv\Lib\site-packages --force-reinstall
pause