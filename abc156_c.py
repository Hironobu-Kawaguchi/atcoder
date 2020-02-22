# https://atcoder.jp/contests/abc156/tasks/abc156_c

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
INF = 1001001001

N = int(input())
X = list(map(int, (input().split())))

ans = INF
for i in range(1, 101):
    tmp = 0
    for j in range(N):
        tmp += (X[j] - i) * (X[j] - i)
    ans = min(ans, tmp)

print(ans)
