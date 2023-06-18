# https://atcoder.jp/contests/abc293/tasks/abc293_e
# from numba import njit
# from functools import lru_cache


def main():
    A, X, M = map(int, input().split())

    if A == 1:
        result = X % M
    else:
        result = (1 - pow(A, X, M * (A - 1))) // (1 - A)

    print(result % M)

if __name__ == '__main__':
    main()


# import sys
# input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# # sys.setrecursionlimit(10 ** 7)
# import numpy as np

# def main():
#     A, X, M = map(int, input().split())
#     b = np.array([[A,1], [0,1]], dtype=int)
#     res = np.eye(2,2,dtype=int)
#     # print(b)
#     # print(res)
#     while X:
#         if X%2:
#             res = res @ b
#             res %= M
#         b = b @ b
#         b %= M
#         X //= 2
#     # print(res)
#     print(res[0,1])

# main()


# # https://atcoder.jp/contests/abc293/editorial/5966
# A,X,M=map(int,input().split())
# if A==1:
#   print(X%M)
# else:
#   print( (pow(A,X,M*(A-1))-1) // (A-1))


# RE
# import sys
# input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# # sys.setrecursionlimit(10 ** 7)
# MOD = 998244353

# def main():
#     A, X, M = map(int, input().split())
#     A %= M

#     if A==1:
#         ans = X % M
#     else:
#         ans = (pow(A, X, MOD) - 1) * pow(A-1, M-2, MOD)
#         ans %= M
#     print(ans)

# main()
