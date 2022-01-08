# https://atcoder.jp/contests/ABC234/tasks/abc234_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def main():
    K = int(input())
    if K==1:
        return '2'
    K -= 1
    now = 2
    while K>now:
        K -= now
        now *= 2
    ans = '2'
    while now>1:
        now //= 2
        if K>now:
            ans += '2'
            K -= now
        else:
            ans += '0'
    return ans

print(main())



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
