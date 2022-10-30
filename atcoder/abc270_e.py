# https://atcoder.jp/contests/abc270/tasks/abc270_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import copy

N, K = map(int, input().split())
A = list(map(int, (input().split())))
e = copy.copy(A)
e.sort()
pre = 0

for i in range(N):
    r = N - i
    num = r * (e[i]-pre)
    if ((num<=K) and (i != N-1)):
        K -= num
        pre = e[i]
    else:
        pre += K//r
        for j in range(N):
            A[j] = max(0, A[j]-pre)
        K %= r
        for j in range(N):
            if K>0 and A[j]>0:
                A[j] -= 1
                K -= 1
        break

print(*A)



# import sys
# input = sys.stdin.buffer.readline
# # sys.setrecursionlimit(10 ** 7)

# N, K = map(int, input().split())
# A = list(map(int, (input().split())))

# l, r = 0, K+2
# while r-l>1:
#     now = (l+r)//2
#     tmp = 0
#     for a in A:
#         tmp += min(now, a)
#     if tmp>K:
#         r = now
#     else:
#         l = now
# # print(l, r)

# for i in range(N):
#     tmp = min(A[i], l)
#     A[i] -= tmp
#     K -= tmp

# for i in range(N):
#     if K==0: break
#     if A[i]: 
#         A[i] -= 1
#         K -= 1

# print(*A)
