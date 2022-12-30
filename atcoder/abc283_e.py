# https://atcoder.jp/contests/ABC283/tasks/abc283_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
INF = 1001001

H, W = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(H)]
# print(A)

dp = [[INF]*2 for _ in range(H)]   # 0: 反転なし, 1:反転あり
dp[0][0] = 0
dp[0][1] = 1
# print(dp)

def chk(i, flg=0):
    tmp_list = [[-1]*W for _ in range(2)]
    for ii in range(2):
        for j in range(W):
            if flg and ii==0:
                tmp_list[ii][j] = 1 - A[i+ii][j]
            else:
                tmp_list[ii][j] = A[i+ii][j]
    cnt = [[0]*W for _ in range(2)]
    for ii in range(2):
        for j in range(W-1):
            if tmp_list[ii][j]==tmp_list[ii][j+1]:
                cnt[ii][j] += 1
                cnt[ii][j+1] += 1
    for j in range(W):
        if tmp_list[0][j]==tmp_list[1][j]:
            cnt[0][j] += 1
            cnt[1][j] += 1
    print(i, flg, cnt)
    ret = True
    for ii in range(2):
        for j in range(W):
            if cnt[ii][j]==0:
                ret = False
                break
    return ret

for i in range(H-1):
    if chk(i):
        # print(i, "chk0")
        dp[i+1][0] = min(dp[i+1][0], dp[i][0])
        dp[i+1][1] = min(dp[i+1][1], dp[i][1] + 1)
    if chk(i, 1):
        # print(i, "chk1")
        dp[i+1][0] = min(dp[i+1][0], dp[i][1])
        dp[i+1][1] = min(dp[i+1][1], dp[i][0] + 1)
print(dp)

