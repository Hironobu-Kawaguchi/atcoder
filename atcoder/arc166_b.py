# https://atcoder.jp/contests/arc166/tasks/arc166_b
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

from math import gcd
INF = 10**30

N, a, b, c = map(int, input().split())
A = list(map(int, (input().split())))
abc = [a, b, c]
# rest = [[] for _ in range(3)]
# for i, x in enumerate([a, b, c]):
#     for j in range(N):
#         rest[i].append((x - A[j]%x)%x)
# print(rest)
rest_d = []
for i in range(N):
    d = {}
    for j in range(1<<3):
        lcm = 1
        for k in range(3):
            if j & (1<<k):
                lcm = lcm * abc[k] // gcd(lcm, abc[k])
        cost = (lcm - A[i]%lcm)%lcm
        d[j] = cost
    rest_d.append(d)
# print(rest_d)

dp = [[INF] * (1<<3) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for j in range(1<<3):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        for k, v in rest_d[i].items():
            dp[i+1][j|k] = min(dp[i+1][j|k], dp[i][j] + v)
# for i in range(N+1):
    # print(dp[i])
print(dp[N][(1<<3)-1])
