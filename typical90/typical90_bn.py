# https://atcoder.jp/contests/typical90/tasks/typical90_bn

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
L, R = [], []
for i in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
ans = 0.0
for i in range(N-1):
    for j in range(i+1, N):
        sm = 0
        tt = 0
        for xi in range(L[i], R[i]+1):
            for xj in range(L[j], R[j]+1):
                sm += 1
                if xi>xj: tt += 1
        ans += tt / sm
print(ans)
