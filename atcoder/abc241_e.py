# https://atcoder.jp/contests/abc241/tasks/abc241_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def main():
    N, K = map(int, input().split())
    A = list(map(int, (input().split())))
    gone = [-1]*N
    cumsum = [0]*N
    idx = [-1]*(N+1)
    now = 0
    for i in range(N+1):
        if gone[now%N]!=-1:
            start = gone[now%N]
            start_sm = cumsum[now%N]
            cycle = i - gone[now%N]
            cycle_sm = now - cumsum[now%N]
            break
        else:
            gone[now%N] = i
            cumsum[now%N] = now
            now += A[now%N]
            idx[i] = now
        # print(i, now, gone, cumsum)
    # print(start, start_sm, cycle, cycle_sm, idx)
    ans = start_sm
    if K<=start:
        ans = idx[K-1]
    else:
        K -= start
        ans += cycle_sm * (K // cycle)
        for i in range(K%cycle):
            ans += A[ans%N]
    print(ans)
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
