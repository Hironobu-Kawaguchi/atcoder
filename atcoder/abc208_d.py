# https://atcoder.jp/contests/abc208/tasks/abc208_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
INF = 1001001001

N, M = map(int, input().split())
d = [[INF]*N for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    d[A-1][B-1] = C

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j: continue
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
            if d[i][j]!=INF:
                ans += d[i][j]
print(ans)


# TLE
# import sys
# input = sys.stdin.buffer.readline
# # sys.setrecursionlimit(10 ** 7)
# INF = 4001001001

# N, M = map(int, input().split())
# d = [[[INF]*N for _ in range(N)] for _ in range(N)]
# for i in range(M):
#     A, B, C = map(int, input().split())
#     d[0][A-1][B-1] = C
#     # for x in range(N):
#     #     d[x][A-1][B-1] = C
# for k in range(N):
#     # for x in range(N):
#         # if k>x: break
#     if k!=0:
#         for i in range(N):
#             for j in range(N):
#                 d[k][i][j] = d[k-1][i][j]
#     for i in range(N):
#         # if i>x: break
#         for j in range(N):
#             # if j>x: break
#             # d[x][i][j] = min(d[x][i][j], d[x][i][k] + d[x][k][j])
#             d[k][i][j] = min(d[k][i][j], d[k][i][k] + d[k][k][j])
# ans = 0
# for i in range(N):
#     for j in range(N):
#         if i==j: continue
#         if d[N-1][i][j]==INF: continue
#         for x in range(N):
#             if d[x][i][j]==INF: continue
#             # print(i+1, j+1, x+1, d[x][i][j])
#             ans += d[x][i][j]
# print(ans)
