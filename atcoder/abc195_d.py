# https://atcoder.jp/contests/abc195/tasks/abc195_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import bisect


N, M, Q = map(int, input().split())
VW = []
for i in range(N):
    _w, _v = map(int, input().split())
    VW.append((_v, _w))
VW.sort(reverse=True)
# print(VW)
X = list(map(int, (input().split())))

def query(L, R):
    x = X[:L-1] + X[R:]
    x.sort()
    # print(x)
    ans = 0
    for v, w in VW:
        idx = bisect.bisect_left(x, w)
        if idx==len(x): continue
        ans += v
        x.pop(idx)
        # print(idx, v, w, x)
    print(ans)
    return

for i in range(Q):
    L, R = map(int, input().split())
    query(L, R)




# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
