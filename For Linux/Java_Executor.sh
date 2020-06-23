#!/bin/sh
: '
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
'
echo WELCOME TO EXECUTOR
echo Garvit Joshi\(garvitjoshi9@gmail.com\)
echo USER:$USERNAME
while true
do
	python3 Filename_java.py
	filename="Input.txt"
	while IFS= read -r line
	do
	        javac "$line"
	done <"$filename"
	python3 Filename_class.py
	filename1="Input.txt"
	echo "-------------------------------"
	echo "OUTPUT:"
	echo "-------------------------------"
	while IFS= read -r line
	do
	        java "$line"
	done <"$filename1"
	echo "-------------------------------"
	echo "-------------------------------"
	read -p "Press [Enter] key to continue..." readEnterKey
done
exit
