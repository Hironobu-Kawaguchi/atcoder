# https://atcoder.jp/contests/newjudge-2308-algorithm/tasks/abc244_c
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
done = [False] * (2*N+1)

for i in range(N+1):
    for j in range(2*N+1):
        if done[j]: continue
        done[j] = True
        print(j+1, flush=True)
        break
    res = int(input())
    done[res-1] = True
    if res == 0:
        done[j] = True
        break

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
