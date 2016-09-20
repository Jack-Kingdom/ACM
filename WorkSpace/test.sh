#!/usr/bin/env bash
if [ -e "\*.cpp" ]
then
    g++ *.cpp -std=c++11 -o test.out
    ./test.out < ./input.txt > ./output.txt
    rm test.out
elif [ -e "\*.py" ]
then
    python3 *.py < ./input.txt > ./output.txt
fi