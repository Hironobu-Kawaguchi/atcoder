# https://atcoder.jp/contests/arc121/tasks/arc121_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append((x, i))
    Y.append((y, i))
X.sort()
Y.sort()
cand = []
cand.append((X[-1][0]-X[0][0], min(X[-1][1], X[0][1]), max(X[-1][1], X[0][1])))
cand.append((X[-2][0]-X[0][0], min(X[-2][1], X[0][1]), max(X[-2][1], X[0][1])))
cand.append((X[-1][0]-X[1][0], min(X[-1][1], X[1][1]), max(X[-1][1], X[1][1])))
cand.append((Y[-1][0]-Y[0][0], min(Y[-1][1], Y[0][1]), max(Y[-1][1], Y[0][1])))
cand.append((Y[-2][0]-Y[0][0], min(Y[-2][1], Y[0][1]), max(Y[-2][1], Y[0][1])))
cand.append((Y[-1][0]-Y[1][0], min(Y[-1][1], Y[1][1]), max(Y[-1][1], Y[1][1])))

cand.sort(reverse=True)
# print(cand)

if cand[0][1]!=cand[1][1] or cand[0][2]!=cand[1][2]:
    print(cand[1][0])
else:
    print(cand[2][0])


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
