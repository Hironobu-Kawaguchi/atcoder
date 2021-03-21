# https://atcoder.jp/contests/abc183/tasks/abc183_d
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

n, w = map(int, input().split())
# s, t, p = [], [], []
nums = [0]*(200005)
for i in range(n):
    _s, _t, _p = map(int, input().split())
    # s.append(_s)
    # t.append(_t)
    # p.append(_p)
    nums[_s] += _p
    nums[_t] -= _p

ans = 'Yes'
now = 0
for i in range(200005):
    now += nums[i]
    if now>w:
        ans = 'No'
print(ans)

# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
