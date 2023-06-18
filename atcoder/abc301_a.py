# https://atcoder.jp/contests/abc301/tasks/abc301_a
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input()

T, A = 0, 0
for s in S:
    if s=='T':
        T += 1
    else:
        A += 1

if T>A:
    print('T')
elif T<A:
    print('A')
else:
    if S[-1]=='T':
        print('A')
    else:
        print('T')

# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
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
