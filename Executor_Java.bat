@ECHO OFF
ECHO                                        WELCOME TO EXECUTOR
ECHO                                                         -Garvit Joshi(garvitjoshi9@gmail.com)
ECHO                                                          USER:%USERNAME%
cd /d "%~dp0"
:first
ECHO LOOKING FOR FILES IN:"%~dp0"
echo.
ECHO Name Of Java Executable Files Present In Folder Are:
python Filename_java.py
set /p inp1=<Input.txt
echo.
ECHO =====================================================================================================================
javac %inp1%
ECHO =====================================================================================================================
echo.
ECHO Name Of Java Executable Class Present In Folder Are:
python Filename_class.py
set /p inp2=<Input.txt
echo.
ECHO =====================================================================================================================
javac %inp1%
ECHO =====================================================================================================================
echo.
ECHO =====================================================================================================================
ECHO OUTPUT:
ECHO =====================================================================================================================
java %inp2%
ECHO =====================================================================================================================
echo.
pause
ECHO =====================================================================================================================
ECHO *********************************************************************************************************************
ECHO =====================================================================================================================
goto first