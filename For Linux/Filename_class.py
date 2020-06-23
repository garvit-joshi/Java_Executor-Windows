'''
	Java Executor-Executes Java files with simplicity
    Copyright (C) 2020  Garvit Joshi

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''
#GitHub Link:https://github.com/garvit-joshi/Java_Executor
import glob, os
import sys
a=sys.path
count=0
l=0
os.chdir(a[0])
ifile=open("Input.txt","w")
i=1
for file in glob.glob("*.class"):
	if(count%2==0):
		print(i,".",file,end="")
		g=str(i)
		l=len(file)+len(g)
	else:
		print("".rjust(40-l,' '),i,".",file)
	i=i+1
	count=count+1
print("")
flag=1
while flag==1:
	f=int(input("Enter The File No. You Want To Execute:"))
	i=1
	for file in glob.glob("*.class"):
		if(i==f):
			flag=0
			x=file
			break
		i=i+1
	if flag==1:
		print("File Not Found!!\nPlease Enter Again:")
x= x[:-6]
ifile.write(x)
ifile.write("\n");
ifile.close()
