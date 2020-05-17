# https://atcoder.jp/contests/abc168/tasks/abc168_c

# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

import math
A,B,H,M = map(int, input().split())
a = H*60 + M
b = M*12
c = min(abs(a-b), 60*12-abs(a-b))
ans = math.sqrt(A*A+B*B-2*A*B*math.cos(c*2*math.pi/(60*12)))
print(ans)

# N = int(input())
# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
