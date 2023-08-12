# https://atcoder.jp/contests/abc307/tasks/abc307_c
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

Ha, Wa = map(int, input().split())
A = [input().rstrip() for _ in range(Ha)]
Hb, Wb = map(int, input().split())
B = [input().rstrip() for _ in range(Hb)]
Hx, Wx = map(int, input().split())
X = [input().rstrip() for _ in range(Hx)]

Hs = max(Ha, Hb)
H = Hs * 2 + Hx
Ws = max(Wa, Wb)
W = Ws * 2 + Wx

def check(ia, ja, ib, jb):
    c = [[False] * W for _ in range(H)]
    for i in range(Ha):
        for j in range(Wa):
            if A[i][j]=="#":
                # print(ia+i, ja+j)
                c[ia+i][ja+j] = True
    for i in range(Hb):
        for j in range(Wb):
            if B[i][j]=="#":
                c[ib+i][jb+j] = True
    # if ia==3 and ja==4 and ib==3 and jb==4:
    #     for i in range(H):
    #         print(c[i])
    for i in range(H):
        for j in range(W):
            if Hs<=i<Hs+Hx and Ws<=j<Ws+Wx:
                if (X[i-Hs][j-Ws]=="#") ^ (c[i][j]):
                    return False
            else:
                if c[i][j]:
                    return False
    # print(ia, ja, ib, jb, c)
    return True

for ia in range(H-Hs):
    for ja in range(W-Ws):
        for ib in range(H-Hs):
            for jb in range(W-Ws):
                if check(ia, ja, ib, jb):
                    print("Yes")
                    exit()
print("No")


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
