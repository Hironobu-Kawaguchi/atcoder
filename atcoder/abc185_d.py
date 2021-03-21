# https://atcoder.jp/contests/abc185/tasks/abc185_d
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()

def main():
    N, M = map(int, input().split())
    if M==0:
        print(1)
        return
    A = list(map(int, (input().split())))
    A.sort()
    A.append(N+1)
    white_cnts = []

    now = 1
    for a in A:
        if now < a:
            white_cnts.append(a-now)
        now = a+1
    # print(white_cnts)
    if len(white_cnts)==0:
        print(0)
        return
    k = min(white_cnts)

    ans = 0
    for white in white_cnts:
        ans += (white + k - 1) // k
    print(ans)

main()


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
