# https://atcoder.jp/contests/abc271/tasks/abc272_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))

odd, even = [], []
for a in A:
    if a%2:
        odd.append(a)
    else:
        even.append(a)
odd.sort()
even.sort()
ans = 0
if len(odd)>=2:
    ans = max(ans, odd[-1]+odd[-2])
if len(even)>=2:
    ans = max(ans, even[-1]+even[-2])
if ans==0:
    print(-1)
else:
    print(ans)
