# https://atcoder.jp/contests/typical90/tasks/typical90_cc
# 二次元累積和

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
cum = [[0]*5001 for _ in range(5001)]
for i in range(N):
    a, b = map(int, input().split())
    cum[a][b] += 1

for i in range(5000):
    for j in range(5000):
        if j!=0:
            cum[i][j] += cum[i][j-1]
for j in range(5000):
    for i in range(5000):
        if i!=0:
            cum[i][j] += cum[i-1][j]

# for i in range(10):
#     print(*cum[i][:10])

ans = 0
for i in range(5000-K-1):
    for j in range(5000-K-1):
        ans = max(ans, cum[i][j] + cum[i+K+1][j+K+1] - cum[i][j+K+1] - cum[i+K+1][j])
print(ans)
