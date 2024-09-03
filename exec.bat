@echo off
set PYTHON_PATH="D:\Thiago\TP - Home Office\BI\Python\extrair_resultados_sql\.venv\Scripts\python.exe" 
set SCRIPT_PATH="D:\Thiago\TP - Home Office\BI\Python\extrair_resultados_sql\main.py"
set JSON_PATH="D:\Thiago\TP - Home Office\BI\Python\extrair_resultados_sql\config\config.json"
set INI_PATH="D:\Thiago\TP - Home Office\BI\Python\extrair_resultados_sql\query\query.ini"

%PYTHON_PATH% %SCRIPT_PATH% %JSON_PATH% %INI_PATH%
pause



