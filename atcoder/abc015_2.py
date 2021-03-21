# https://atcoder.jp/contests/abc015/tasks/abc015_2

import math

N = int(input())
A = list(map(int, input().split()))

summ, cnt = 0, 0
for i in range(N):
    if A[i]  == 0:
        continue
    else:
        cnt += 1
        summ += A[i]

ans = math.ceil(summ / cnt)

print(ans)
