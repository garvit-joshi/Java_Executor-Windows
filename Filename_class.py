import glob, os
os.chdir("C:/JavaProgs")                              #Default Directory
file1=open("List.txt","a")
i=1
for file in glob.glob("*.class"):
	file1.write(file)
	file1.write("\n")
	print(i,".",file)
	i=i+1;
file1.write("==============================\n")
file1.write("******************************")
