# https://atcoder.jp/contests/typical90/tasks/typical90_z

import sys
# from numba import njit
from collections import Counter
sys.setrecursionlimit(10 ** 7)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

col = [-1] * N

def dfs(pos, color):
    col[pos] = color
    for nxt in G[pos]:
        if col[nxt]==-1:
            dfs(nxt, 1 - color)
    return

dfs(0, 0)
print(*col, file=sys.stderr)
cnt = Counter(col)
if cnt[0]>=cnt[1]:
    ans = [i+1 for i in range(N) if col[i]==0]
else:
    ans = [i+1 for i in range(N) if col[i]==1]
print(*ans[:N//2])


# TLE
# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

# MAX_N = 100005
# col = [-1] * MAX_N
# to = [[] for _ in range(MAX_N)]

# def dfs(pos, color):
#     col[pos] = color
#     for nxt in to[pos]:
#         if col[nxt]==-1:
#             dfs(nxt, 1-color)
#     return

# N = int(input())
# for i in range(N-1):
#     a, b = map(int, input().split())
#     to[a-1].append(b-1)
#     to[b-1].append(a-1)

# dfs(0, 0)
# zeros, ones = 0, 0
# for i in range(N):
#     if col[i]==0: zeros += 1
#     else:         ones += 1
# if zeros>=ones:
#     c = 0
# else:
#     c = 1
# cnt = 0
# ans = []
# for i in range(N):
#     if col[i]==c:
#         ans.append(i+1)
#         cnt += 1
#     if cnt*2==N:
#         break
# print(*ans)
