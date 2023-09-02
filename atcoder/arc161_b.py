# https://atcoder.jp/contests/arc161/tasks/arc161_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
import bisect

cand = [-1]
for i in range(60):
    for j in range(i+1, 60):
        for k in range(j+1, 60):
            cand.append(2**i + 2**j + 2**k)
cand.sort()

def main():
    N = int(input())
    idx = bisect.bisect_right(cand, N)
    print(cand[idx-1])

T = int(input())
for ti in range(T):
    main()


# import sys
# input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# # sys.setrecursionlimit(10 ** 7)

# def main():
#     N = int(input())
#     bit = bin(N)[2:]
#     # print(N, bit)
#     ans = ''
#     cnt = 0
#     if bit.count('1')>=3:
#         for c in bit:
#             if c=='1' and cnt <3:
#                 cnt += 1
#                 ans += '1'
#             else:
#                 ans += '0'
#     elif len(bit)<=3:
#         print(-1)
#         return
#     elif bit.count('1')==1:
#         ans = '1' * 3 + '0' * (len(bit)-4)
#     else:   # 1が2個
#         idx_list = []
#         for i, c in enumerate(bit):
#             if c=='1':
#                 idx_list.append(i)
#         if idx_list[1]<=len(bit)-3:
#             ans = '1' + '0' * idx_list[1] + '1' * 2 + '0' * (len(bit)-idx_list[1]-3)
#         else:
#             ans = '1' * 3 + '0' * (len(bit)-4)

#     # print(N, len(bit), bit, ans)
#     print(int(ans, 2))

# T = int(input())
# for ti in range(T):
#     main()

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
