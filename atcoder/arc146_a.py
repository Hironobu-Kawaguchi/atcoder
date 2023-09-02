# https://atcoder.jp/contests/arc146/tasks/arc146_a
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))
A.sort(reverse=True)

ans = []
for i in range(3):
    for j in range(3):
        if i==j: continue
        for k in range(3):
            if i==k or j==k: continue
            ans.append(int(str(A[i]) + str(A[j]) + str(A[k])))
ans.sort(reverse=True)
print(ans[0])
