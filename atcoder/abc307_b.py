# https://atcoder.jp/contests/abc307/tasks/abc307_b
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = [input().rstrip() for _ in range(N)]
# print(S)

def kaibun(s1, s2):
    a = s1 + s2
    b = a[::-1]
    return a==b

for i in range(N):
    for j in range(N):
        if i==j: continue
        if kaibun(S[i], S[j]):
            print("Yes")
            exit()
print("No")


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
