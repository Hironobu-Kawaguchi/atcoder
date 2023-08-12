# https://atcoder.jp/contests/abc308/tasks/abc308_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
from functools import cmp_to_key

N = int(input())
ab = []
for i in range(N):
    a, b = map(int, input().split())
    b += a
    ab.append([a, b])
# print(ab, file=sys.stderr)

p = [i for i in range(N)]

# sort順の比較関数を定義
def compare(x, y):
    if ab[x][0]*ab[y][1] > ab[y][0]*ab[x][1]:
        return -1
    elif ab[x][0]*ab[y][1] == ab[y][0]*ab[x][1] and x < y:
        return -1
    else:
        return 1

p.sort(key=cmp_to_key(compare))
print(*[i+1 for i in p])



# import math

# N = int(input())
# ab = []
# for i in range(N):
#     a, b = map(int, input().split())
#     g = math.gcd(a, b)
#     a //= g
#     b //= g
#     b += a
#     rate = 10**20 * a // b
#     ab.append([rate, N-i-1, a, b])
# # div = ab[0][1]
# # for i in range(1, N):
# #     div = div * ab[i][2] // math.gcd(div, ab[i][2])
# # for i in range(N):
# #     tmp = div // ab[i][2]
# #     ab[i][0] *= tmp
# ab.sort(reverse=True)
# # print(ab)
# for i in range(N):
#     print(N-ab[i][1], end=" ")

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
