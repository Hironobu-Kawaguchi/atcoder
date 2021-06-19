# https://atcoder.jp/contests/arc122/tasks/arc122_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

MOD = 10**9+7
# N = 10
N = int(input())
A = list(map(int, (input().split())))
dp = [[0,0] for _ in range(N)]
dp[0][0] = 1
dp[0][1] = 1
for i in range(N-1):
    dp[i+1][0] = dp[i][0] + dp[i][1]
    dp[i+1][0] %= MOD
    dp[i+1][1] = dp[i][0]
    dp[i+1][1] %= MOD

# for i in range(N):
#     print(dp[i-1][0]+dp[i-1][1], dp[i-1][0], dp[i-1][1])
# print(dp[N-1][0]+dp[N-1][1], dp[N-1][0], dp[N-1][1])
ans = 0
for i in range(N):
    if i==0:
        ans += (A[i] * (dp[N-2][0] + dp[N-2][1]))%MOD
    elif i==1 or i==N-1:
        ans += (A[i] * (dp[N-2][0] - dp[N-2][1]))%MOD
    else:
        # ans += (A[i] * (dp[N-2][0] + dp[N-2][1] - 2*(2**(N-4))))%MOD
        ans += (A[i] * (dp[N-2][0] + dp[N-2][1] - 2*(dp[i-2][0]*dp[N-i-2][0])))%MOD
    ans %= MOD
    # print(i, ans)
if N==1:
    print(A[0])
else:
    print(ans)


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
