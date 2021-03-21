# https://atcoder.jp/contests/abc170/tasks/abc170_e

import bisect
import sys
INF = 1001001001
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# @njit(cache=True)

N, Q = map(int, input().split())
lst = [[] for _ in range(2*10**5+10)]
A = []        # 園児のレート
now = [0]*N   # 園児が今どの幼稚園か
bs = 0  # 幼稚園の数
for i in range(N):
    _a, _b = map(int, input().split())
    bs = max(bs, _b)
    _b -= 1
    bisect.insort_left(lst[_b], _a)
    A.append(_a)
    now[i] = _b

mx = [INF]*bs
ans = INF
for i in range(bs):
    if lst[i]:
        mx[i] = lst[i][-1]
        ans = min(ans, mx[i])
# print(lst)
# print(mx)
# print(ans)

for j in range(Q):
    _c, _d = map(int, input().split())
    _c -= 1;_d -= 1
    lst[now[_c]].pop(bisect.bisect_left(lst[now[_c]], A[_c]))
    if lst[now[_c]]:
        mx[now[_c]] = lst[now[_c]][-1]
    else:
        mx[now[_c]] = INF
    bisect.insort_left(lst[_d], A[_c])
    if lst[_d]:
        mx[_d] = lst[_d][-1]
    else:
        mx[_d] = INF
    ans = min(mx)
    print(ans)

# def main():
# #     # @lru_cache(None)
# #     # def dfs():
# #     #     return
# #     A, B = map(int, input().split())
# #     print(A*B)
#     if Y%2:
#         return 'No'
#     Y //= 2
#     if X <= Y <= 2*X:
#         return 'Yes'
#     else:
#         return 'No'

# print(main())


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
