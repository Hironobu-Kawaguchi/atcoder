# https://atcoder.jp/contests/typical90/tasks/typical90_bd

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, S = map(int, input().split())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [set([0])]
for i in range(N):
    s = dp[-1]
    ss = set()
    for j in s:
        if j+A[i]<=S: ss.add(j+A[i])
        if j+B[i]<=S: ss.add(j+B[i])
    dp.append(ss)

if S in dp[-1]:
    ans = ""
    now = S
    for i in range(N-1, -1, -1):
        if now - A[i] in dp[i]:
            ans += 'A'
            now -= A[i]
        else:
            ans += 'B'
            now -= B[i]
    print(ans[::-1])
else:
    print("Impossible")
