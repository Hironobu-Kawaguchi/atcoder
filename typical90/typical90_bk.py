# https://atcoder.jp/contests/typical90/tasks/typical90_bk

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

H, W = map(int, input().split())
P = [[int(i) for i in input().split()] for _ in range(H)]
# print(P)

ans = 0
for bi in range(1, 1<<H):
    A = 0
    tmp = []
    for j in range(H):
        if bi>>j&1:
            A += 1
            tmp.append(P[j])
    # print(A, len(tmp), tmp)
    cnt = defaultdict(int)
    for j in range(W):
        for k in range(A):
            if k!=0 and tmp[k][j]!=tmp[0][j]:
                break
        else:
            cnt[tmp[0][j]] += 1
    B = 0
    for k, v in cnt.items():
        B = max(B, v)
    ans = max(ans, A*B)
print(ans)
