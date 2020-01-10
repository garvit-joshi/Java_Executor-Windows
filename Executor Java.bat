@ECHO OFF
ECHO                                        WELCOME TO EXECUTOR
ECHO                                                         -Garvit Joshi
cd C:\JavaProgs
:first
ECHO Name Of Java Executable Files Present In Folder Are:
python Filename_java.py
set /p "input=>Enter The File You Want To Execute:"
javac %input%.java
ECHO Name Of Python Executable Class Present In Folder Are:
python Filename_class.py
set /p "input=>Enter The Class You Want To Run:"
ECHO ===============================
ECHO OUTPUT:
ECHO ===============================
java %input%
ECHO ===============================
pause
ECHO =======================================================
ECHO *******************************************************
ECHO =======================================================
goto first
