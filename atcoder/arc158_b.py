# https://atcoder.jp/contests/arc158/tasks/arc158_b
# from numba import njit
# from functools import lru_cache

import bisect
from itertools import permutations

N = int(input())
X = list(map(int, input().split()))
X.sort()
idx_set = set()
for i in range(3):
    idx_set.add(i)
for i in range(N-3, N):
    idx_set.add(i)
zero_idx = bisect.bisect_left(X, 0)
for i in range(3):
    if zero_idx + i >= N:
        break
    idx_set.add(zero_idx + i)
for i in range(3):
    if zero_idx - 1 - i < 0:
        break
    idx_set.add(zero_idx - 1 - i)
# print(idx_set)
ans_min, ans_max = 10**18, -10**18

for i, j, k in permutations(idx_set, 3):
    # print(i, j, k, (X[i] + X[j] + X[k])/(X[i] * X[j] * X[k]))
    ans_min = min(ans_min, (X[i] + X[j] + X[k])/(X[i] * X[j] * X[k]))
    ans_max = max(ans_max, (X[i] + X[j] + X[k])/(X[i] * X[j] * X[k]))
print(ans_min)
print(ans_max)


# import sys
# input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# # sys.setrecursionlimit(10 ** 7)
# import bisect
# from itertools import permutations
# INF = 1001001001.0

# def main():
#     N = int(input())
#     x = list(map(int, (input().split())))
#     x.sort()
#     st = set([0,1, N-2, N-1])
#     zero_idx = bisect.bisect_left(x, 0)
#     for i in range(2):
#         if zero_idx - 1 - i<0: break
#         st.add(zero_idx - 1 - i)
#     for i in range(2):
#         if zero_idx + i>N-1: break
#         st.add(zero_idx + i)
#     # print(st)
#     mx = -INF
#     mn = INF
#     for i in range(N):
#         for j, k in permutations(st, 2):
#             if i==j or i==k: continue
#             # print(i, j, k)
#             tmp = (x[i]+x[j]+x[k])/(x[i]*x[j]*x[k])
#             mx = max(mx, tmp)
#             mn = min(mn, tmp)
#     print(mn)
#     print(mx)
#     return


# main()

