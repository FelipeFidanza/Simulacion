@echo off
echo Activando entorno virtual...
call venv\Scripts\activate.bat


echo.
echo Generando ejecutable con PyInstaller...
pyinstaller simulacion.spec

echo.
echo Proceso completado. El ejecutable esta en la carpeta dist/
pause
