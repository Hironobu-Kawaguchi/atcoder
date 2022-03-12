# https://atcoder.jp/contests/abc243/tasks/abc243_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def main():
    N = int(input())
    X, Y = [], []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = input()

    d = dict()
    for i in range(N):
        if (Y[i], S[i]) not in d:
            d[(Y[i], S[i])] = X[i]
        elif S[i]=='L':
            d[(Y[i], S[i])] = max(X[i], d[(Y[i], S[i])])
        else:
            d[(Y[i], S[i])] = min(X[i], d[(Y[i], S[i])])
    ans = 'No'
    for (y, s), x in d.items():
        if s=='L' and (y, 'R') in d:
            if x>d[(y, 'R')]:
                print('Yes')
                return
        elif s=='R' and (y, 'L') in d:
            if x<d[(y, 'L')]:
                print('Yes')
                return
    print('No')
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
