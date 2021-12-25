# https://atcoder.jp/contests/typical90/tasks/typical90_bc
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# # sys.setrecursionlimit(10 ** 7)
# from itertools import combinations

# N, P, Q = map(int, input().split())
# A = list(map(int, (input().split())))
# # for i in range(N):
# #     A[i] %= P
# ans = 0
# for i, j, k, l, m in combinations(range(N), 5):
#     v = ((((A[i] * A[j] % P) * A[k] % P) * A[l] % P) * A[m]) % P
#     if v == Q:
#         ans += 1
# print(ans)


import sys
input = sys.stdin.buffer.readline

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
Answer = 0
 
for i in range(0, N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            for l in range(k + 1, N):
                for m in range(l + 1, N):
                    v = ((((A[i] * A[j] % P) * A[k] % P) * A[l] % P) * A[m]) % P
                    if v == Q:
                        Answer += 1
 
print(Answer)



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
