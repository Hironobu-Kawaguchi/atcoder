# https://atcoder.jp/contests/cf16-final/tasks/codefestival_2016_final_b

import math
N = int(input())
x = math.ceil((-1+math.sqrt(1+8*N))/2)
y = x*(x+1)//2 - N
for i in range(1, x+1):
    if i != y:
        print(i)
