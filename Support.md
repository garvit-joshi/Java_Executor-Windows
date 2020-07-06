# Support To Notepad++
1. After Installing Notepad++, goto C:\Users\\%USERNAME%\AppData\Roaming\Notepad++\shortcuts.xml [Path](Screenshots/1.Path.PNG)<br>
2. Add A Line inside ```<UserDefinedCommands> </UserDefinedCommands> ``` <br>
Line: ``` <Command name="Java_Executor" Ctrl="no" Alt="no" Shift="no" Key="117">cmd /k cd $(CURRENT_DIRECTORY) &amp;&amp; &quot;$(CURRENT_DIRECTORY)/Executor_Java.bat&quot;</Command> ``` <br> <img src =Screenshots/2.shortcuts.xml.PNG width="650" height="350" alt="Input Processes"> [Line](Screenshots/2.shortcuts.xml.PNG)
3. Save The changes and restart notepad++. <br>
4. Put Executor_Java.bat, Filename_class.py, Filename_java.py in the folder where you will keep all the java files. [Example](Screenshots/3.Files) <br>
5. After making a java code press ```F6``` in notepad++ and Executor.bat will run successfully. [Output](Screenshots/4.Output.PNG)<br>
<img src =Screenshots/4.Output.PNG width="650" height="350" alt="Output">