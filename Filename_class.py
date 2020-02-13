import glob, os
import sys
a=sys.path
count=0
l=0
os.chdir(a[0])
file1=open("List.txt","a")
i=1
for file in glob.glob("*.class"):
	file1.write(file)
	file1.write("\n")
	if(count%2==0):
		print(i,".",file,end="")
		g=str(i)
		l=len(file)+len(g)
	else:
		print("".rjust(40-l,' '),i,".",file)
	i=i+1
	count=count+1
file1.write("==============================\n")
file1.write("******************************")
