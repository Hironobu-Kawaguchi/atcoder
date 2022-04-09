# https://atcoder.jp/contests/arc138/tasks/arc138_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import bisect
INF = 1001001001

def main():
    N, K = map(int, input().split())
    A = list(map(int, (input().split())))

    s = sum(A[:K])
    min_left = min(A[:K])
    max_right = max(A[K:])
    # print(s, min_left, max_right)
    if min_left>=max_right:
        print(-1)
        return

    left_list, left_idx, right_list, right_idx = [], [], [], []
    for i in range(K-1, -1, -1):
        if A[i]<max_right:
            left_list.append(A[i])
            left_idx.append(i)
            max_right = A[i]
    for j in range(K, N):
        if A[j]>min_left:
            right_list.append(A[j])
            right_idx.append(j)
            min_left = A[j]
    left_list.reverse()
    left_idx.reverse()
    # print(left_list)
    # print(left_idx)
    # print(right_list)
    # print(right_idx)

    ans = INF
    for i, l in enumerate(left_list):
        idx = bisect.bisect_right(right_list, l)
        ans = min(ans, right_idx[idx] - left_idx[i])
        # print(i, idx, ans)
    print(ans)

main()

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
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
