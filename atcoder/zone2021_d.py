# https://atcoder.jp/contests/zone2021/tasks/zone2021_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

from queue import Queue

S = input()
Tj, Th = '', ''
flg = True
for i in range(len(S)):
    if S[i]=='R':
        flg = 1-flg
        continue
    if flg: Tj += S[i]
    else:   Th += S[i]
if flg: tmp = Th[::-1] + Tj
else:   tmp = Tj[::-1] + Th
# print(tmp)

ans = []
for i in range(len(tmp)):
    if len(ans)==0:
        ans.append(tmp[i])
    elif ans[-1]==tmp[i]:
        ans.pop()
    else:
        ans.append(tmp[i])
print(''.join(ans))


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
