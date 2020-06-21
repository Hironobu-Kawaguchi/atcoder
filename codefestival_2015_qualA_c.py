# https://atcoder.jp/contests/code-festival-2015-quala/tasks/codefestival_2015_qualA_c
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

N, T = map(int, input().split())
C = []
sumA = 0
for i in range(N):
    _a, _b = map(int, input().split())
    sumA += _a
    C.append(_a-_b)
C.sort(reverse=True)
ans = 0
while sumA > T:
    sumA -= C[ans]
    ans += 1
    if ans >= N and sumA > T:
        ans = -1
        break
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
