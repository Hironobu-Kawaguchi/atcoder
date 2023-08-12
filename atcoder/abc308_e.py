# https://atcoder.jp/contests/abc308/tasks/abc308_e
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
import copy

N = int(input())
A = list(map(int, (input().split())))
S = input()
# print(S)

dp = [[[0] * 4 for _ in range(4)] for _ in range(4)]
dp[3][3][3] = 1
# print(dp)

for i in range(N):
    dp_pre = copy.copy(dp)
    if S[i]=="M":
        dp[A[i]][3][3] += dp_pre[3][3][3]
    elif S[i]=="E":
        for m in range(3):
            dp[m][A[i]][3] += dp_pre[m][3][3]
    elif S[i]=="X":
        for m in range(3):
            for e in range(3):
                dp[m][e][A[i]] += dp_pre[m][e][3]

def mex(m, e, x):
    tmp_set = set([m, e, x])
    for i in range(4):
        if i not in tmp_set:
            return i

ans = 0
for m in range(3):
    for e in range(3):
        for x in range(3):
            ans += dp[m][e][x] * mex(m, e, x)
print(ans)
