# https://atcoder.jp/contests/abc273/tasks/abc273_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import bisect

H, W, rs, cs = map(int, input().split())
rs -= 1; cs -= 1
rd = {}
cd = {}

N = int(input())
for i in range(N):
    r, c = map(int, input().split())
    r -= 1; c -= 1
    if r in rd: rd[r].append(c)
    else:       rd[r] = [c]
    if c in cd: cd[c].append(r)
    else:       cd[c] = [r]
for k, v in rd.items():
    v.extend([-1, W])
    v.sort()
for k, v in cd.items():
    v.extend([-1, H])
    v.sort()
# print(rd)
# print(cd)

r, c = rs, cs
Q = int(input())
for qi in range(Q):
    # print(r+1, c+1)
    d, l = input().split()
    l = int(l)
    if d=='L':
        if r not in rd:
            c = max(c-l, 0)
        else:
            idx = bisect.bisect(rd[r], c) - 1
            c = max(c-l, rd[r][idx]+1)
    elif d=='R':
        if r not in rd:
            c = min(c+l, W-1)
        else:
            idx = bisect.bisect(rd[r], c)
            c = min(c+l, rd[r][idx]-1)
    elif d=='U':
        if c not in cd:
            r = max(r-l, 0)
        else:
            idx = bisect.bisect(cd[c], r) - 1
            r = max(r-l, cd[c][idx]+1)
    else:
        if c not in cd:
            r = min(r+l, H-1)
        else:
            idx = bisect.bisect(cd[c], r)
            r = min(r+l, cd[c][idx]-1)
    print(r+1, c+1)



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
