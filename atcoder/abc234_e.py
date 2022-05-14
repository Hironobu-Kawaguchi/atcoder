# https://atcoder.jp/contests/ABC234/tasks/abc234_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import bisect

def gen_tosasu():
    res = set()
    for first in range(1,10):
        for d in range(-9,9):
            s = ''
            now = first
            for i in range(18):
                s += str(now)
                res.add(int(s))
                now += d
                if now<0 or now>9: break
    return sorted(list(res))

X = int(input())
tosasu = gen_tosasu()
# print(len(tosasu), tosasu)
print(tosasu[bisect.bisect_left(tosasu, X)])



# WA
# X = input()
# X = list(map(int, list(X)))
# # print(X)
# n = len(X)

# def create_same(X):
#     mx = 0
#     for a in X: 
#         mx = max(mx, a)
#     for i in range(n):
#         X[i] = mx
#     return X

# def ok(X, diff):
#     last = X[0] + (X[1]-X[0]+diff) * (n-1)
#     if last<0 or last>9:
#         return False
#     for i in range(2, n):
#         if X[i] > X[0] + (X[1]-X[0]+diff) * i:
#             return False
#     return True

# def create_diff(X, diff):
#     X[1] += diff
#     for i in range(2, n):
#         X[i] = X[0] + (X[1]-X[0]) * i
#     return X

# def create_plus_one(X):
#     X[0] += 1
#     diff = X[0] // (n-1)
#     for i in range(1,n):
#         X[i] = X[i-1] - diff
#     return X

# def main(X):
#     if n<=2:
#         return X
#     elif n>=11:
#         return create_same(X)
#     for diff in range(10):
#         if ok(X, diff):
#             return create_diff(X, diff)    
#     return create_plus_one(X)

# print(''.join(list(map(str,(main(X))))))


