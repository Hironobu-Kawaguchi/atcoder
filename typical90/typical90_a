# https://atcoder.jp/contests/typical90/tasks/typical90_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, L = map(int, input().split())
K = int(input())
A = list(map(int, (input().split())))

def chk(now):
    cnt = 0
    tmp = 0
    for i in range(N):
        if A[i] - tmp >= now:
            cnt += 1
            tmp = A[i]
    if L - tmp < now:
        cnt -= 1
    if cnt >= K:
        return True
    return False

l = 0
r = L
while l+1<r:
    now = (l+r)//2
    # print(l, r, now)
    if chk(now):
        l = now
    else:
        r = now
print(l)


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
