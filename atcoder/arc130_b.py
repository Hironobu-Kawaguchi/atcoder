# https://atcoder.jp/contests/arc130/tasks/arc130_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

H, W, C, Q = map(int, input().split())
query = []
for qi in range(Q):
    t, n ,c = map(int, input().split())
    n -= 1
    c -= 1
    query.append((t, n, c))
# print(query)

hs, ws = dict(), dict()
seth, setw = set(), set()
for t, n ,c in query[::-1]:
    if t == 1:
        if n in seth: continue
        seth.add(n)
        hs[n] = (c, len(setw))
    else:
        if n in setw: continue
        setw.add(n)
        ws[n] = (c, len(seth))
# print(seth, hs)
# print(setw, ws)
ans = [0] * C
for n, (c, cnt) in hs.items():
    ans[c] += W - cnt
for n, (c, cnt) in ws.items():
    ans[c] += H - cnt
print(*ans)


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
