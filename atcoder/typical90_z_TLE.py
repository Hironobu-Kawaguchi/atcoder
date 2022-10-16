# https://atcoder.jp/contests/typical90/tasks/typical90_z
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

MAX_N = 100005
col = [-1] * MAX_N
to = [[] for _ in range(MAX_N)]

def dfs(pos, color):
    col[pos] = color
    for nxt in to[pos]:
        if col[nxt]==-1:
            dfs(nxt, 1-color)
    return

N = int(input())
for i in range(N-1):
    a, b = map(int, input().split())
    to[a-1].append(b-1)
    to[b-1].append(a-1)

dfs(0, 0)
zeros, ones = 0, 0
for i in range(N):
    if col[i]==0: zeros += 1
    else:         ones += 1
if zeros>=ones:
    c = 0
else:
    c = 1
cnt = 0
ans = []
for i in range(N):
    if col[i]==c:
        ans.append(i+1)
        cnt += 1
    if cnt*2==N:
        break
print(*ans)


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
