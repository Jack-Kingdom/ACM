#!/usr/bin/env bash
g++ *.cpp -std=c++11 -o test.out
./test.out < ./input.txt > output.txt
rm test.out