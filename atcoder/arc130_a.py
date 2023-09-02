# https://atcoder.jp/contests/arc130/tasks/arc130_a
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input().rstrip()

seq = []
now = 1
for i in range(N-1):
    if S[i] == S[i+1]:
        now += 1
    else:
        if now>1:
            seq.append(now)
        now = 1
if now>1:
    seq.append(now)
ans = 0
for c in seq:
    ans += c*(c-1)//2
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
