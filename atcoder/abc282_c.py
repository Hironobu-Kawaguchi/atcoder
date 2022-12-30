# https://atcoder.jp/contests/ABC282/tasks/abc282_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input()
# print(S)
ans = ""
flg = True
for i in range(N):
    if S[i]=='"': 
        flg = 1 - flg
        ans += S[i]
    elif S[i]==',':
        if flg:
            ans += '.'
        else:
            ans += S[i]
    else:
        ans += S[i]
print(ans)


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
