# https://atcoder.jp/contests/arc138/tasks/arc138_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def main():
    N = int(input())
    A = list(map(int, (input().split())))
    A_sort = sorted(A)
    ans = 0
    middle_num = A_sort[N//2]
    for i in range(N//2, N):
        ans += A_sort[i]
    B = []
    middle_num_count = 0
    for i in range(N):
        if A[i]==middle_num:
            middle_num_count += 1
        if A[i]>=middle_num:
            B.append(1)
        else:
            B.append(-1)
    # print(B)
    # print(middle_num_count, middle_num)
    if middle_num_count>1:
        tmp = middle_num_count - 1
        for i in range(N-1, -1, -1):
            if A[i]==middle_num:
                B[i] = -1
                tmp -= 1
            if tmp==0:
                break
    # print(B)
    C = [0]
    for b in B:
        C.append(C[-1]+b)
    # print(C)
    max_c = -1
    best_idx = 0
    for i in range(1, N+1):
        if C[i]>max_c:
            max_c = C[i]
            best_idx = i
    # print(best_idx, max_c)
    print(best_idx, ans)

    return

main()


# TLE
# import sys
# input = sys.stdin.buffer.readline
# # sys.setrecursionlimit(10 ** 7)
# import numpy as np

# def main():
#     N = int(input())
#     A = list(map(int, (input().split())))
#     argsort = np.argsort(-np.array(A))
#     # print(argsort)
#     # flg = [True]*N
#     # for i in range(N):
#     #     for j in range(2*i):
#     #         flg[(N+j-argsort[i])%N] = False
#     #     print(i, flg)
#     def point(idx):
#         ret = 0
#         flg = [True] * N
#         for i in range(N):
#             if i%2:
#                 for j in range(i//2, N):
#                     if flg[(j+idx)%N]:
#                         flg[(j+idx)%N] = False
#                         break
#             else:
#                 for j in range(i//2, N):
#                     if flg[argsort[j]]:
#                         flg[argsort[j]] = False
#                         ret += A[argsort[j]]
#                         # print(idx, i, ret, flg)
#                         break
#         # print(flg)
#         return ret

#     ans = 0
#     best_idx = 0
#     for i in range(N):
#         tmp = point(i)
#         # print(i, tmp)
#         if tmp>ans:
#             ans = tmp
#             best_idx = i
#     print(best_idx, ans)

#     return

# main()
