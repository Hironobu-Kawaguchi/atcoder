# https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_c

import numpy as np
from numba import njit
import sys
# import copy
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
# A = np.array(list(map(int, (input().split()))))
A = np.array(input().split(), dtype=np.int64)
# A = list(map(int, (input().split())))
# nd = np.zeros((N,N), dtype=bool)
# print(*A)

# @njit('(i8[::1],)', cache=True)
@njit(cache=True)
def loop(A):
    for i in range(K):
        # cnt = [0]*N
        cnt = np.zeros_like(A)
        for j, x in enumerate(A):
            # nd[j, max(j-A[j],0):min(j+A[j]+1,N)] = True
            l = max(j-x,0)
            r = min(j+x+1,N)
            cnt[l] += 1
            if r<N:
                cnt[r] -= 1
            # for k in range(max(j-A[j],0), min(j+A[j]+1,N)):
            #     cnt[k] += 1
        # print(nd)
        # A = np.count_nonzero(nd, axis=0)
        # print(cnt)
        A = np.cumsum(cnt)
        if A[0] == A[N-1] == N:
            break
        # print(*A)
    return A

A = loop(A)
print(*A)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
