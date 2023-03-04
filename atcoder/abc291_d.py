# https://atcoder.jp/contests/abc291/tasks/abc291_d
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
MOD = 998244353

N = int(input())
AB = [[] for _ in range(2)]
for i in range(N):
    a, b = map(int, input().split())
    AB[0].append(a)
    AB[1].append(b)
# print(AB)

dp = [[0]*2 for _ in range(N)]
# print(dp)
dp[0][0] = 1
dp[0][1] = 1

for i in range(N-1):
    for j in range(2):
        for k in range(2):
            if AB[j][i+1]!=AB[k][i]:
                dp[i+1][j] += dp[i][k]
                dp[i+1][j] %= MOD
ans = (dp[N-1][0] + dp[N-1][1]) % MOD
print(ans)


# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# import sys
# it = map(int, sys.stdin.buffer.read().split())
# N = next(it)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
