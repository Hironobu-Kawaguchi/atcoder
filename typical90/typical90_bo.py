# https://atcoder.jp/contests/typical90/tasks/typical90_bo
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# # sys.setrecursionlimit(10 ** 7)

N, K = input().split()
K = int(K)

def f(s):
    x = 0
    for i in range(len(s)):
        x *= 8
        x += int(s[i])
    # print(x)
    ret = ''
    if x==0: ret = '0'
    while x>0:
        x, mod = divmod(x, 9)
        if mod==8:
            ret += '5'
        else:
            ret += str(mod)
    return ret[::-1]

for i in range(K):
    N = f(N)
print(N)


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
