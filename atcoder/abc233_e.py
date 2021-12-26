# https://atcoder.jp/contests/abc233/tasks/abc233_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

X = input()
N = len(X)

cumX = [0]
for i in range(N):
    cumX.append(cumX[-1] + int(X[i]))
# print(cumX)

for i in range(N,-1,-1):
    if cumX[i]>=10:
        div, mod = divmod(cumX[i], 10)
        cumX[i-1] += div
        cumX[i] = mod
# print(cumX)

ans = ''
for i in range(N+1):
    if i==0 and cumX[i]==0: continue
    ans += str(cumX[i])
print(ans)


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
