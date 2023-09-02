# https://atcoder.jp/contests/abc292/tasks/abc292_e
# from numba import njit
# from functools import lru_cache


import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)

reachable = [[] for _ in range(N)]

def dfs(start, u):
    visited[u] = True
    if start!=u:
        reachable[start].append(u)
    for v in G[u]:
        if visited[v]: continue
        dfs(start, v)
    return

for u in range(N):
    visited = [False]*N
    visited[u] = True
    dfs(u, u)
# print(reachable, file=sys.stderr)

ans = -M
for u in range(N):
    ans += len(reachable[u])
print(ans)


#WA
# INF = 1001001001001
# def main():
#     N, M = map(int, input().split())
#     A = [[INF]*N for _ in range(N)]
#     for i in range(M):
#         u, v = map(int, input().split())
#         A[u-1][v-1] = 1
#     print(A)
#     for k in range(N):
#         for i in range(N):
#             for j in range(N):
#                 A[i][j] = min(A[i][j], A[i][k] + A[k][j])
#     print(A)
#     ans = -M
#     for i in range(N):
#         for j in range(N):
#             if i==j: continue
#             if A[i][j]<INF:
#                 ans += 1
#     print(ans)
#     return

# main()


# TLE
# import sys
# input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# # sys.setrecursionlimit(10 ** 7)
# INF = 1001001001001

# def main():
#     N, M = map(int, input().split())
#     A = [[INF]*N for _ in range(N)]
#     for i in range(M):
#         u, v = map(int, input().split())
#         A[u-1][v-1] = 1
#     print(A)
#     for k in range(N):
#         for i in range(N):
#             for j in range(N):
#                 A[i][j] = min(A[i][j], A[i][k] + A[k][j])
#     print(A)
#     ans = -M
#     for i in range(N):
#         for j in range(N):
#             if i==j: continue
#             if A[i][j]<INF:
#                 ans += 1
#     print(ans)
#     return

# main()

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
