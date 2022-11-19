# https://atcoder.jp/contests/abc211/tasks/abc211_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

idx = {"H":0 , "2B":1 , "3B":2 , "HR":3}
S = [input() for _ in range(4)]
cnt = [0]*4
for c in S:
    cnt[idx[c]] += 1
ans = "Yes"
for i in range(4):
    if cnt[i]!=1:
        ans = "No"
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
