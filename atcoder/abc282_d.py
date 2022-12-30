# https://atcoder.jp/contests/ABC282/tasks/abc282_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
color = [-1]*N
for i in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
flg = True

def dfs(now, c, g):
    global flg
    if color[now]==-1:
        color[now] = c
    for nxt in G[now]:
        if color[nxt]==-1:
            dfs(nxt, 4*g+1-c, g)
        elif color[nxt]==c:
            flg = False
    return

g = 0
for i in range(N):
    if color[i]==-1:
        dfs(i, 2*g, g)
        g += 1

cnt = [0]*(2*g)
for i in range(N):
    cnt[color[i]] += 1
# print(cnt)

ans = 0
if flg:
    for i in range(2*g):
        ans += cnt[i]*(N-cnt[i])
    ans //= 2
    ans -= M
print(ans)


# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
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
