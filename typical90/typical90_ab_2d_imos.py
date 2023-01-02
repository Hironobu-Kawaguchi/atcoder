# https://atcoder.jp/contests/typical90/tasks/typical90_ab

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

imos = [[0]*1001 for _ in range(1001)]
N = int(input())
for i in range(N):
    lx, ly, rx, ry = map(int, input().split())
    imos[lx][ly] += 1
    imos[rx][ry] += 1
    imos[rx][ly] -= 1
    imos[lx][ry] -= 1
# for x in range(5):
    # print(imos[x][:5])

for y in range(1001):
    for x in range(1000):
        imos[x+1][y] += imos[x][y]
for x in range(1001):
    for y in range(1000):
        imos[x][y+1] += imos[x][y]
# for x in range(5):
    # print(imos[x][:5])

A = [0]*(N+1)
for x in range(1000):
    for y in range(1000):
        # print(imos[x][y])
        A[imos[x][y]] += 1
for i in range(1, N+1):
    print(A[i])
