# https://atcoder.jp/contests/abc221/tasks/abc221_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
# from collections import Counter

N = input().rstrip()
N = list(N)

ans = 0
for i in range(1<<len(N)):
    x, y = [], []
    for bi in range(len(N)):
        if (i>>bi)&1:
            x.append(N[bi])
        else:
            y.append(N[bi])
    if len(x)==0 or len(y)==0: continue
    x.sort(reverse=True)
    y.sort(reverse=True)
    # print(x, y)
    x = int(''.join(x))
    y = int(''.join(y))
    ans = max(ans, x*y)

print(ans)


# cnt = [0]*10
# for c in N:
#     cnt[int(c)] += 1
# # print(cnt)
# x, y = '', ''
# now = 9
# for i in range(len(N)):
#     while cnt[now]==0:
#         now -= 1
#     cnt[now] -= 1
#     if i%2:
#         y += str(now)
#     else:
#         x += str(now)
# print(x, y)
# ans = int(x) * int(y)
# print(ans)        


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
