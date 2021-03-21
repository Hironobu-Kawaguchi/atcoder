# https://atcoder.jp/contests/abc169/tasks/abc169_e

import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A, B = [], []
for i in range(N):
    _a, _b = map(int, (input().split()))
    A.append(_a); B.append(_b)
A.sort(); B.sort()

if N%2:     # 奇数
    ans = B[N//2] - A[N//2] + 1
else:       # 偶数
    ans = (B[N//2] + B[N//2-1]) - (A[N//2] + A[N//2-1]) + 1
print(ans)

# N = int(input())
# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
