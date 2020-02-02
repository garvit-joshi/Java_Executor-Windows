@ECHO OFF
ECHO                                        WELCOME TO EXECUTOR
ECHO                                                         -Garvit Joshi(garvitjoshi9@gmail.com)
ECHO                                                          USER:%USERNAME%
cd %cd% 
:first
ECHO Name Of Java Executable Files Present In Folder Are:
python Filename_java.py
set /p "input=Enter The File You Want To Execute:"
javac %input%.java
ECHO Name Of Java Executable Class Present In Folder Are:
python Filename_class.py
set /p "input=Enter The Class You Want To Run:"
color 0A
ECHO ===============================
ECHO OUTPUT:
ECHO ===============================
java %input%
ECHO.
ECHO ===============================
color 0F
pause
ECHO =======================================================
ECHO *******************************************************
ECHO =======================================================
goto first
