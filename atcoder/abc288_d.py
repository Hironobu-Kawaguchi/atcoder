# https://atcoder.jp/contests/abc288/tasks/abc288_d

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
A = list(map(int, input().split()))

s = [[0]*(N+1) for _ in range(K)]
for i in range(N):
    s[i%K][i+1] = A[i]
for k in range(K):
    for i in range(N):
        s[k][i+1] += s[k][i]
# print(s)

Q = int(input())
for qi in range(Q):
    l, r = map(int, input().split())
    l -= 1
    ns = []
    for k in range(K):
        ns.append(s[k][r] - s[k][l])
    ns.sort()
    if ns[0]==ns[-1]:
        print("Yes")
    else:
        print("No")
