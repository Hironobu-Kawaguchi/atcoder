# https://atcoder.jp/contests/genocon2021/tasks/genocon2021_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

INF = 1001001001

s = input()
t = input()

dp = [[-INF] * (len(t)+1) for _ in range(len(s)+1)]
dp[0][0] = 0
# print(dp)
dps = [[''] * (len(t)+1) for _ in range(len(s)+1)]
dpt = [[''] * (len(t)+1) for _ in range(len(s)+1)]
# print(dps)

for i in range(len(s)+1):
    for j in range(len(t)+1):
        if i!=0:
            if dp[i][j] < dp[i-1][j] - 5:
                dp[i][j] = dp[i-1][j] - 5
                dps[i][j] = dps[i-1][j] + s[i-1]
                dpt[i][j] = dpt[i-1][j] + '-'
        if j!=0:
            if dp[i][j] < dp[i][j-1] - 5:
                dp[i][j] = dp[i][j-1] - 5
                dps[i][j] = dps[i][j-1] + '-'
                dpt[i][j] = dpt[i][j-1] + t[j-1]
        if i!=0 and j!=0:
            if s[i-1]==t[j-1]:
                if dp[i][j] < dp[i-1][j-1] + 1:
                    dp[i][j] = dp[i-1][j-1] + 1
                    dps[i][j] = dps[i-1][j-1] + s[i-1]
                    dpt[i][j] = dpt[i-1][j-1] + t[j-1]
            else:
                if dp[i][j] < dp[i-1][j-1] - 3:
                    dp[i][j] = dp[i-1][j-1] - 3
                    dps[i][j] = dps[i-1][j-1] + s[i-1]
                    dpt[i][j] = dpt[i-1][j-1] + t[j-1]
# print(dp[len(s)][len(t)])
print(dps[len(s)][len(t)])
print(dpt[len(s)][len(t)])


# def sim(x, y):
#     if x=='-' or y=='-':
#         return -5
#     elif x==y:
#         return 1
#     else:
#         return -3
        
# def pairwise_alignment(s, t):
#     ret = 0
#     for i in range(len(s)):
#         ret += sim(s[i], t[i])
#     return ret

# print(pairwise_alignment("AGTTGAA-TTT", "-GTCGGACTTT"))
# print(pairwise_alignment("AGT-TGAATTT", "-GTCGGACTTT"))

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
