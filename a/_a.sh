#!/bin/bash

mkfifo tmp

# python _a_runner.py < tmp | tee output.txt | python _a_tester.py| tee input.txt  > tmp
# python arc168_b.py < tmp | tee output.txt | python _a_tester.py| tee input.txt  > tmp
python abc332_d_check.py < tmp | tee output.txt | python _a_tester.py| tee input.txt  > tmp

# /opt/homebrew/bin/g++-12 -std=c++17 -O2 _a_runner.cpp
# ./a.out < tmp | tee output.txt | python _a_tester.py | tee input.txt > tmp

rm tmp
