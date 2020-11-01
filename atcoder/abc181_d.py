# https://atcoder.jp/contests/abc181/tasks/abc181_c
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

from collections import Counter

def main():
    S = input()
    Scnt = Counter(S)
    if len(S) >= 3:
        n = 3
    else:
        n = len(S)
    for i in range(10**n):
        if i%8==0:
            tmp = str(i).zfill(n)
            # print(tmp)
            cnt = Counter(tmp)
            flg = True
            for k, v in cnt.items():
                if Scnt[k] < v:
                    flg = False
            if flg:
                print("Yes")
                return
    print("No")
    return

main()


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
