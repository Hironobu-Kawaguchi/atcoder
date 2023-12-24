# https://atcoder.jp/contests/abc331/tasks/abc331_c

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

import bisect

N = int(input())
A = list(map(int, input().split()))

B = [(a, i) for i, a in enumerate(A)]
B.sort()
# print(*B, file=sys.stderr)

cum = [0] * (N + 1)
for i in range(N):
    cum[i + 1] = cum[i] + B[i][0]

A.sort()
ans = [0] * N
for i in range(N):
    idx = bisect.bisect_right(A, B[i][0])
    ans[B[i][1]] = cum[-1] - cum[idx]

print(*ans)
