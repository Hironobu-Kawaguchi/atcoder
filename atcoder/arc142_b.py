# https://atcoder.jp/contests/arc142/tasks/arc142_b

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
ans = [[0]*N for _ in range(N)]

now = 1
for i in range(0, N, 2):
    for j in range(N):
        ans[i][j] = now
        now += 1
for i in range(1, N, 2):
    for j in range(N):
        ans[i][j] = now
        now += 1

for i in range(N):
    print(*ans[i])
