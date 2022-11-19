# https://atcoder.jp/contests/abc211/tasks/abc211_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
MOD = 10**9+7
chokudai = ['c' , 'h' , 'o' , 'k' , 'u' , 'd' , 'a' , 'i']
dp = [[0]*8 for _ in range(100005)]
S = input()
N = len(S)
for i in range(N):
    for j in range(8):
        dp[i+1][j] = dp[i][j]
        if S[i]==chokudai[j]:
            if j==0: dp[i+1][j] += 1
            else:    dp[i+1][j] += dp[i+1][j-1]
        dp[i+1][j] %= MOD
print(dp[N][7])


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
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
