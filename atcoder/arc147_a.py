# https://atcoder.jp/contests/arc147/tasks/arc147_a
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
from collections import deque

N = int(input())
A = list(map(int, (input().split())))
A.sort()
q = deque(A)

ans = 0
while len(q)>1:
    v =  q.pop()
    if v%q[0]:
        q.appendleft(v%q[0])
    ans += 1
print(ans)
