import glob, os
import sys
a=sys.path
count=0
os.chdir(a[0])
file1=open("List.txt","w")
i=1
for file in glob.glob("*.java"):
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
