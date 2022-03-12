# https://atcoder.jp/contests/typical90/tasks/typical90_cf
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input()
ans = 0
last = [-1]*2
for i in range(N):
    if S[i]=='o': 
        last[0] = i
    else:
        last[1] = i
    if last[0]==-1 or last[1]==-1: 
        continue
    ans += min(last[0], last[1]) + 1
    # print(ans, last)
print(ans)


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
