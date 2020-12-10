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
#GitHub Link:https://github.com/garvit-joshi/Java_Executor-Windows
import glob
COUNT=0
ifile=open("Input.txt","w")
SERIAL_NO=1
WORD_LENGTH=10
for file in glob.glob("*.class"):
    if COUNT%2==0:
        print(SERIAL_NO,".",file,end="")
        SERIAL_LENGTH=str(SERIAL_NO)
        WORD_LENGTH=len(file)+len(SERIAL_LENGTH)
    else:
        print("".rjust(40-WORD_LENGTH,' '),SERIAL_NO,".",file)
    SERIAL_NO = SERIAL_NO + 1
    COUNT=COUNT+1
print("")
FLAG=1
FILE_NAME=-1
FILE_NO=0
while FLAG in (1,2):
    FLAG=1
    try:
        FILE_NO=int(input("Enter The File No. You Want To Execute:"))
    except ValueError:
        print("Oops!  \nThat was no valid number.  \nTry again...")
        FLAG=2
    SERIAL_NO=1
    if FLAG!=2:
        for file in glob.glob("*.class"):
            if SERIAL_NO==FILE_NO:
                FLAG=0
                FILE_NAME=file
                break
            SERIAL_NO = SERIAL_NO + 1
            FLAG=1
    if FLAG==1:
        print("File Not Found!!\nPlease Try Again...")
FILE_NAME= FILE_NAME[:-6]
ifile.write(FILE_NAME)
ifile.write("\n")
ifile.close()
