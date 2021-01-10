# https://atcoder.jp/contests/abc186/tasks/abc186_e
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

from math import gcd

def main():
    N, S, K = map(int, input().split())
    K %= N    ### N より大きくても無意味
    g = gcd(N,K)
    if S%g:
            print(-1)
    else:
        x = N-1
        while N*x

    if N%K==0 or N%(K-(N%K))==0:
        # print(N%K, (N-S)%K)
        if (N-S)%K:
            print(-1)
        else:
            print((N-S)//K)
    else:
        # print(N%K, (N-S)%(N%K))
        rest = S
        diff = N%K
        if rest < diff:
            rest = K - rest
            diff = K - diff
        print(rest, diff)
        if rest%diff:
            print(-1)
        else:
            print(((rest//diff)*N-S)//K)
    # ans = 0
    # print(ans)
    return

T = int(input())
for t in range(T):
    main()


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
