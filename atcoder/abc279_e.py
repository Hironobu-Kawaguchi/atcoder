# https://atcoder.jp/contests/ABC279/tasks/abc279_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
A = list(map(int, (input().split())))

mem = [set() for _ in range(N)]
now = 0
for i in range(M):
    mem[A[i]-1], mem[A[i]] = mem[A[i]], mem[A[i]-1]
    mem[now].add(i)
    if A[i]==now+1: now += 1
    elif A[i]==now: now -= 1
# print(mem)

ans = [-1]*M
for i in range(N):
    for j in mem[i]:
        ans[j] = i+1
for a in ans:
    print(a)



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
