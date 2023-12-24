# https://atcoder.jp/contests/abc321/tasks/abc321_b
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, X = map(int, input().split())
A = list(map(int, (input().split())))
A.sort()
sm = sum(A)

def ok(y):
    res = sm
    if y > A[-1]:
        res -= A[0]
    elif y < A[0]:
        res -= A[-1]
    else:
        res += y - A[0] - A[-1]
    if res >= X:
        return True

for y in range(0, 101):
    if ok(y):
        print(y)
        exit()
else:
    print(-1)
