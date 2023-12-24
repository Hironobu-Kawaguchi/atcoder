# https://atcoder.jp/contests/abc328/tasks/abc328_c

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, Q = map(int, input().split())
S = input()

cum = [0] * (N)
for i in range(N-1):
    cum[i+1] = cum[i] + (1 if S[i] == S[i+1] else 0)
# print(cum, file=sys.stderr)

for qi in range(Q):
    l, r = map(int, input().split())
    print(cum[r-1] - cum[l-1])
