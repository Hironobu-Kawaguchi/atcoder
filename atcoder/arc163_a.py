# https://atcoder.jp/contests/arc163/tasks/arc163_a
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

def main():
    N = int(input())
    S = input()
    # print(S, file=sys.stderr)
    # 2つに分割できればOK
    for i in range(1, N):
        if S[i]>S[0]:
            print("Yes")
            return
        elif S[i]==S[0]:
            if S[i:] > S[:i]:
                print("Yes")
                return
    print("No")
    return

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
