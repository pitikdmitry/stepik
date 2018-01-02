#!/bin/bash
n=${1}
if [[ n -eq 0 ]]
then
echo "No students"
elif [[ ${n} -eq 1 ]]
then
echo "1 student"
elif [[ ${n} -eq 2 ]]
then
echo "2 students"
elif [[ ${n} -eq 3 ]]
then
echo "3 students"
elif [[ ${n} -eq 4 ]]
then
echo "4 students"
else
echo "A lot of students"
fi
