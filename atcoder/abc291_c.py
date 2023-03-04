# https://atcoder.jp/contests/abc291/tasks/abc291_c
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

def main():
    N = int(input())
    # gone = [[False]*(N*2+5) for _ in range(N*2+5)]
    gone = set()
    S = input()
    x, y = N, N
    gone.add((x, y))
    for c in S:
        if c=='R':
            x += 1
        elif c=='L':
            x -= 1
        elif c=='U':
            y += 1
        else:
            y -= 1
        if (x, y) in gone:
            print("Yes")
            return
        gone.add((x, y))
    print("No")
    return

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
