# https://atcoder.jp/contests/abc270/tasks/abc270_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N, X, Y = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
gone = [False] * (N+1)
gone[X] = True
ans = []
stop = False

def dfs(now):
    global ans, stop
    if stop==False: ans.append(now)
    # print(now, ans, gone)
    if now==Y:
        # print(ans)
        stop = True
        return
    for v in G[now]:
        if gone[v]: continue
        gone[v] = True
        dfs(v)
        if stop==False: ans.pop()
    return

dfs(X)
# print(ans)
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
