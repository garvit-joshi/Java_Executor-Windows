#!/bin/sh
echo WELCOME TO EXECUTOR
echo Garvit Joshi\(garvitjoshi9@gmail.com\)
echo USER:$USERNAME
python3 Filename_java.py
filename="Input.txt"
while IFS= read -r line
do
        javac "$line"
done <"$filename"
python3 Filename_class.py
filename1="Input.txt"
while IFS= read -r line
do
        java "$line"
done <"$filename1"
exit
