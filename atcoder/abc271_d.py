# https://atcoder.jp/contests/abc271/tasks/abc271_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, S = map(int, input().split())
card = [[int(i) for i in input().split()] for _ in range(N)]

dp = [[False] * (S+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    for j in range(S+1):
        if dp[i][j]==False: continue
        if j+card[i][0]<=S: dp[i+1][j+card[i][0]]=True
        if j+card[i][1]<=S: dp[i+1][j+card[i][1]]=True
if dp[N][S]:
    print('Yes')
    ans = ''
    now = S
    for i in range(N-1, -1, -1):
        if now>=card[i][0] and dp[i][now-card[i][0]]:
            ans += 'H'
            now -= card[i][0]
        else:
            ans += 'T'
            now -= card[i][1]
    print(ans[::-1])
else:
    print('No')
