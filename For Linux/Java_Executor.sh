#!/bin/bashs
echo WELCOME TO EXECUTOR
echo                                                         -Garvit Joshi\(garvitjoshi9@gmail.com\)
echo                                                          USER:$USERNAME
python3 Filename_java.py
ls -l "Input.txt"
filename="Input.txt"
while IFS= read -r line
do
        echo "$line"
done <"$filename"
exit
