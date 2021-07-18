# https://codeforces.com/contest/1530/problem/A

# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)


def main():
    s = input().rstrip()
    ans = 1
    for c in s:
        ans = max(ans, int(c))
    print(ans)
    return

t = int(input())
for _ in range(t):
    main()


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
