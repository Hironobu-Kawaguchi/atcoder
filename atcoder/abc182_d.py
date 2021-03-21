# https://atcoder.jp/contests/abc182/tasks/abc182_d
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
cum = [0]
cum_max = [0]
for a in A:
    cum.append(cum[-1]+a)
    cum_max.append(max(cum_max[-1],cum[-1]))
ans = 0
now = 0
for i in range(N+1):
    ans = max(now+cum_max[i], ans)
    now += cum[i]
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
