# https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_a
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
if N < 600:
    ans = 8
elif N < 800:
    ans = 7
elif N < 1000:
    ans = 6
elif N < 1200:
    ans = 5
elif N < 1400:
    ans = 4
elif N < 1600:
    ans = 3
elif N < 1800:
    ans = 2
else:
    ans = 1
print(ans)




# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
