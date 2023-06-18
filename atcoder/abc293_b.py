# https://atcoder.jp/contests/abc293/tasks/abc293_b
# from numba import njit
# from functools import lru_cache


import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))
called = [False]*N

for i in range(N):
    if not called[i]:
        called[A[i]-1] = True
ans = []
for i in range(N):
    if not called[i]:
        ans.append(i+1)
print(len(ans))
print(*ans)


# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
