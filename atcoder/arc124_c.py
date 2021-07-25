# https://atcoder.jp/contests/arc124/tasks/arc124_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

from math import gcd
import copy

N = int(input())
ab_list = []    ### [[lcm, a, b]]
for i in range(N):
    a, b = map(int, input().split())
    if i==0:
        lcm = a*b//gcd(a, b)
        ab_list.append([lcm, a, b])
        # print(ab_list)
    else:
        cand_set = set()
        for j in range(len(ab_list)):
            a1 = gcd(a, ab_list[j][1])
            b1 = gcd(b, ab_list[j][2])
            lcm1 = a1*b1//gcd(a1, b1)
            cand_set.add((lcm1, a1, b1))
            a2 = gcd(a, ab_list[j][2])
            b2 = gcd(b, ab_list[j][1])
            lcm2 = a2*b2//gcd(a2, b2)
            cand_set.add((lcm2, a2, b2))
        cand_list = list(cand_set)
        cand_list.sort(reverse=True)
        ab_list = []
        for j in range(len(cand_list)):
            ab_list.append(list(cand_list[j]))
            # if j==0 or cand_list[j-1][0]==cand_list[j][0]:
            #     ab_list.append(list(cand_list[j]))

print(ab_list[0][0])


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
