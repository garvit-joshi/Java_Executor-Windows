import glob, os
os.chdir("C:/Users/Garvit Joshi/Documents/JavaProgs")
file1=open("List.txt","w")
i=1
for file in glob.glob("*.java"):
	file1.write(file)
	file1.write("\n")
	print(i,".",file)
	i=i+1;
