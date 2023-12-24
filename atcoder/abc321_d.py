# https://atcoder.jp/contests/abc321/tasks/abc321_d
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

import bisect

N, M, P = map(int, input().split())
A = list(map(int, (input().split())))
B = list(map(int, (input().split())))
A.sort()
B.sort()
# sumA = 0
# cumA = [0]
# for i in range(N):
#     sumA += A[i]
#     cumA.append(sumA)
sumB = 0
cumB = [0]
for i in range(M):
    sumB += B[i]
    cumB.append(sumB)
ans = 0
for i in range(N):
    rest = P - A[i]
    idx = bisect.bisect_right(B, rest)
    ans += A[i] * idx + cumB[idx] + P * (M - idx)
# for i in range(M):
#     rest = P - B[i]
#     idx = bisect.bisect_right(A, rest)
#     ans += B[i] * idx + cumA[idx] + P * (N - idx)

print(ans)
