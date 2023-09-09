# https://atcoder.jp/contests/abc313/tasks/abc313_d
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
A = [0]*N

def f(x):
    print("?", *[y+1 for y in x], flush=True)
    res = int(input())
    return res

B = [0]*(K+1)
t = 0
for i in range(K+1):
    x = []
    for j in range(K+1):
        if i==j: continue
        x.append(j)
    B[i] = f(x)
    t ^= B[i]
for i in range(K+1):
    A[i] = t ^ B[i]

t = 0
for i in range(K-1): t ^= A[i]
for i in range(K+1, N):
    x = []
    for j in range(K-1): x.append(j)
    x.append(i)
    A[i] = t ^ f(x)

print("!", *A)
