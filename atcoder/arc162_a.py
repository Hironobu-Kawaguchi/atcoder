# https://atcoder.jp/contests/arc162/tasks/arc162_a
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)


def main():
    N = int(input())
    P = list(map(int, (input().split())))
    ans = 0
    done = [False] * N
    now = 1
    for i in range(N):
        if P[i] == now:
            ans += 1
            done[P[i]-1] = True
            for j in range(P[i]-1, N):
                if done[j] is False:
                    now = j + 1
                    break
            # print(i, P[i], now)
        done[P[i]-1] = True
    print(ans)


T = int(input())
for _ in range(T):
    main()

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
