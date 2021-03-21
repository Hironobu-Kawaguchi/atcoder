# https://atcoder.jp/contests/arc100/tasks/arc100_a
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
N = int(input())
A = list(map(int, (input().split())))
suma = 0
sumabs = 0
for i in range(N):
    A[i] -= i+1
    suma += A[i]
A.sort()
b = (A[N//2] + A[(N-1)//2])//2
ans = 0
for i in range(N):
    ans += abs(A[i]-b)
print(ans)


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
