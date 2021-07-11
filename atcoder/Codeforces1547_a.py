# https://codeforces.com/contest/1547/problem/A

# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

def main():
    input()
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xf, yf = map(int, input().split())
    ans = abs(xa-xb) + abs(ya-yb)
    if xa==xb==xf and (ya<yf<yb or ya>yf>yb):
        ans += 2
    elif ya==yb==yf and (xa<xf<xb or xa>xf>xb):
        ans += 2
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
