# https://atcoder.jp/contests/abc323/tasks/abc323_c
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]

A_argsort = [i for (a, i) in sorted(zip(A, range(M)), reverse=True)]
print(*A_argsort, file=sys.stderr)

scores = [0] * N
for i in range(N):
    for j in range(M):
        if S[i][j] == 'o':
            scores[i] += A[j]
    scores[i] += i+1
print(*scores, sep='\n', file=sys.stderr)

for i in range(N):
    score = scores[i]
    max_score = max(scores[:i]+scores[i+1:])
    ans = 0
    for j in range(M):
        if score >= max_score: break
        if S[i][A_argsort[j]] == 'o': continue
        score += A[A_argsort[j]]
        ans += 1
    print(ans)
