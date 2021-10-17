# https://atcoder.jp/contests/abc223/tasks/abc223_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
# MOD = 998244353

def main():
    X, Y, A, B, C = map(int, input().split())
    ABC = [A, B, C]
    if (A+X-1)//X + (B+X-1)//X + (C+X-1)//X <= Y:
        return "Yes"
    if (A+Y-1)//Y + (B+Y-1)//Y + (C+Y-1)//Y <= X:
        return "Yes"
    for i in range(3):
        tmp = Y - (ABC[i]+X-1)//X
        if tmp<=0: continue
        if (ABC[(i+1)%3]+tmp-1)//tmp + (ABC[(i+2)%3]+tmp-1)//tmp <= X:
            return "Yes"
    for i in range(3):
        tmp = X - (ABC[i]+Y-1)//Y
        if tmp<=0: continue
        if (ABC[(i+1)%3]+tmp-1)//tmp + (ABC[(i+2)%3]+tmp-1)//tmp <= Y:
            return "Yes"
    return "No"

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
