# https://atcoder.jp/contests/arc122/tasks/arc122_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))
A.sort()
if N%2:
    x = A[N//2] / 2
else:
    x = (A[N//2-1] + A[N//2]) / 4
ans = 0
for i in range(N):
    ans += A[i] - min(A[i], 2*x)
ans /= N
ans += x
print(ans)



# N = int(input())
# A = list(map(int, (input().split())))
# A.sort()
# cumA = [0]
# for i in range(N):
#     cumA.append(cumA[i]+A[i])
# # print(cumA)

# def f(xx, i):
#     res = cumA[N] - cumA[i+1] - xx*(N-(i+1)*2)/2
#     # for i in range(N):
#     #     # res += x + A[i] - min(A[i], 2*x)
#     #     res += xx/2 + A[i] - min(A[i], xx)
#     return res

# def fx(xx):
#     res = 0
#     for i in range(N):
#         res += xx/2 + A[i] - min(A[i], xx)
#     return res

# # for i in range(8):
# #     print(i, fx(i))

# def bisec(l,r, i):
#     # l, r = 0, 10**9
#     # while l+1<r:
#     #     nowl = (l+r)
#     #     # nowl = (l+r)//2
#     #     nowr = (l+r+1)
#     #     # nowr = (l+r+1)//2
#     #     # if f(nowl, i)!=fx(nowl):
#     #     #     print("error", l, r, nowl, i, f(nowl, i), fx(nowl))
#     #     # if f(nowl, i)>f(nowr, i):
#     #     if fx(nowl)>fx(nowr):
#     #         l = max(l, nowl/2)
#     #     else:
#     #         r = min(r, nowr/2)
#     #     # print(l,r)
#     if f(l,i)<f(r,i):
#         return l
#     else:
#         return r
#     # return int(l+r+0.5)
#     # return l

# ans = 1001001001001
# for i in range(N-1):
#     xx = bisec(A[i], A[i+1], i)
#     # print(i, A[i], A[i+1], xx, f(xx, i))
#     ans = min(ans, f(xx, i))

# # xx = bisec(0, 10**9)
# # print(f(xx)/N)
# print(ans/N)

# # print(f(1,0), fx(1))
# # print(f(2,0), fx(2))
# # print(f(3,0), fx(3))
# # print(f(4,1), fx(4))
# # print(f(5,2), fx(5))

