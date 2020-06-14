# https://atcoder.jp/contests/abc170/tasks/abc170_d

import numpy as np
import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, (input().split())))
A.sort()
cnt = np.zeros(10**6+10, dtype=np.int32)
for i in range(N):
    cnt[A[i]] += 1
for i in range(N-1):
    if cnt[A[i]] != 0:
        cnt[A[i]*2::A[i]] = 0
ans = np.count_nonzero(cnt==1)
print(ans)

# from collections import Counter
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# # from numba import njit
# # from functools import lru_cache
# # sys.setrecursionlimit(10 ** 7)

# # @njit('(i8,i8[::1],i4[::1])', cache=True)
# # @njit(cache=True)

# N = int(input())
# A = list(map(int, (input().split())))
# cntA = Counter(A)
# A = sorted(list(set(A)))
# setA = set()
# for k, v in cntA.items():
#     if v==1:
#         setA.add(k)
# # print(setA)
# for i in range(len(A)-1):
#     for j in range(i+1, len(A)):
#         if A[j] % A[i] == 0:
#             if A[j] in setA:
#                 setA.remove(A[j])
# print(len(setA))

# # def main():
# # #     # @lru_cache(None)
# # #     # def dfs():
# # #     #     return
# # #     A, B = map(int, input().split())
# # #     print(A*B)
# #     if Y%2:
# #         return 'No'
# #     Y //= 2
# #     if X <= Y <= 2*X:
# #         return 'Yes'
# #     else:
# #         return 'No'

# # print(main())


# # S = input()
# # n = int(input())
# # N, K = map(int, input().split())
# # l = list(map(int, (input().split())))
# # A = [[int(i) for i in input().split()] for _ in range(N)]
