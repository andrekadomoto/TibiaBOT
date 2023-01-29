call venv\Scripts\activate.bat
start py -m pip install -r requirements.txt --src venv\Lib\site-packages --force-reinstall
pause
deactivate

