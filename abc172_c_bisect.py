# https://atcoder.jp/contests/abc172/tasks/abc172_c

import sys
input = sys.stdin.buffer.readline

import bisect
N, M, K = map(int, input().split())
A = list(map(int, (input().split())))
B = list(map(int, (input().split())))
cumA, cumB = [0], [0]
for a in A:
    cumA.append(cumA[-1]+a)
for b in B:
    cumB.append(cumB[-1]+b)
ans = 0
for i in range(N, -1, -1):
    if cumA[i] > K: continue
    j = bisect.bisect_right(cumB, K-cumA[i])
    ans = max(ans, i+j-1)
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
