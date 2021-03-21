# https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_e
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)

MOD = 10**9+7


H, W = map(int, input().split())
S = ['' for _ in range(H)]
for i in range(H):
    S[i] = input()
wlst = []
hlst = []
k = 0
for i in range(H):
    cnt = 0
    for j in range(W):
        if S[i][j] == '.':
            k += 1
            cnt += 1
        else:
            if cnt > 0:
                wlst.append(cnt)
            cnt = 0
    if cnt > 0:
        wlst.append(cnt)
    cnt = 0
if cnt > 0:
    wlst.append(cnt)
for j in range(W):
    cnt = 0
    for i in range(H):
        if S[i][j] == '.':
            # k += 1
            cnt += 1
        else:
            if cnt > 0:
                hlst.append(cnt)
            cnt = 0
    if cnt > 0:
        hlst.append(cnt)
    cnt = 0
if cnt > 0:
    hlst.append(cnt)

ans = 0
ans = -pow(2,k-1) * k
for x in wlst:
    ans += x * pow(2,k-x) * (pow(2,x)-1)
    ans %= MOD
for x in hlst:
    ans += x * pow(2,k-x) * (pow(2,x)-1)
    ans %= MOD

print(ans)


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
