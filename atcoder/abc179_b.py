# https://atcoder.jp/contests/abc179/tasks/abc179_b

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


n = int(input())
max_cnt = 0
cnt = 0
for i in range(n):
    d1, d2 = map(int, input().split())
    if d1==d2:
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 0
max_cnt = max(max_cnt, cnt)
if max_cnt >= 3:
    print('Yes')
else:
    print('No')

# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
