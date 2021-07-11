# https://codeforces.com/contest/1547/problem/B

# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

from string import ascii_lowercase

t = int(input())
for i in range(t):
    s = input().rstrip()
    # print(ascii_lowercase[:len(s)][::-1])
    l, r = 0, len(s)-1
    ok = True
    for c in ascii_lowercase[:len(s)][::-1]:
        if s[l]==c:
            l += 1
        elif s[r]==c:
            r -= 1
        else:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
