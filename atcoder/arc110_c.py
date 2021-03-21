# https://atcoder.jp/contests/arc110/tasks/arc110_c
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)
# import math

N = int(input())
P = list(map(int, (input().split())))

Q = [0]*N
for i in range(N):
    P[i] -= 1
    Q[P[i]] = i

ans = []
for i in range(N-1,-1,-1):
    now = Q[i]
    for j in range(now, i):
        ans.append(j)
        Q[P[j]] += 1
        Q[P[j+1]] -= 1
        P[j], P[j+1] = P[j+1], P[j]
    if len(ans)>=N:
        ans = -1
        break
if ans==-1:
    print(ans)
elif len(ans)!=N-1:
    print(-1)
else:
    for a in ans:
        print(a+1)


# def main():
#     n = int(input())
#     for a in range(1,38):
#         for b in range(1,26):
#             if pow(3,a) + pow(5,b) == n:
#                 print(a, b)
#                 return
#     print(-1)
#     return

# main()


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
