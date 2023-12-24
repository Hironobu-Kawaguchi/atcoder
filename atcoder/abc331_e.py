# https://atcoder.jp/contests/abc331/tasks/abc331_e

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, M, L = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
bad_set = set()
for i in range(L):
    c, d = map(int, input().split())
    bad_set.add((c, d))
A = [(a[i], i+1) for i in range(N)]
A.sort(reverse=True)
B = [(b[i], i+1) for i in range(M)]
B.sort(reverse=True)

ans = 0
for i in range(N):
    for j in range(M):
        if (A[i][1], B[j][1]) in bad_set:
            continue
        ans = max(ans, A[i][0] + B[j][0])
        break
print(ans)
