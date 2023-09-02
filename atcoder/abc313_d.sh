# !/bin/bash

mkfifo tmp

python abc313_d.py < tmp | tee output.txt | python abc313_d_test.py| tee input.txt  > tmp

# /opt/homebrew/bin/g++-12 -std=c++17 -O2 abc313_d.cpp
# ./a.out < tmp | tee output.txt | python abc313_d_test.py | tee input.txt > tmp

rm tmp
