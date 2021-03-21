# C - Dice and Coin
# https://atcoder.jp/contests/abc126/tasks/abc126_c


import math

N, K = map(int, input().split())
ans = 0

if N > K:
    ans += (N - K) / N

for i in range(min(N, K)):
    logk = math.ceil(math.log2(K / (i+1)))
    ans += 1 / N * (0.5 ** logk)

print(ans)
