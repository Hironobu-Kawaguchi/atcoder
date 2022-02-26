# https://atcoder.jp/contests/typical90/tasks/typical90_bx
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    smA = 0
    for a in A:
        smA += a
    if smA%10:
        print("No")
        return
    target = smA // 10
    cmA = [0]
    for a in A:
        cmA.append(cmA[-1]+a)
    for a in A:
        cmA.append(cmA[-1]+a)
    l = 0
    r = 1
    while r<=2*N:
        if cmA[r] - cmA[l] == target:
            print("Yes")
            return
        elif cmA[r] - cmA[l] > target:
            l += 1
        else:
            r += 1
    print("No")
    return

main()

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
