# https://atcoder.jp/contests/abc183/tasks/abc183_c
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

from itertools import permutations
N, K = map(int, input().split())
T = [[int(i) for i in input().split()] for _ in range(N)]
ans = 0
for x in permutations(range(1,N), N-1):
    # print(x)
    tmp = 0
    i = 0
    for j in x:
        tmp += T[i][j]
        i = j
    tmp += T[j][0]
    if tmp==K: ans += 1
print(ans)

# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
