# https://atcoder.jp/contests/abc244/tasks/abc244_e
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

# A_0=S, A_1=Tなので，K=1は1通り
MOD = 998244353

N, M, K, S, T, X = map(int, input().split())
S -= 1; T -= 1; X -= 1
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

# dp[i][j][k]: A_iがjで，k=0ならXを偶数回，k=1ならXを機数回通ったときの通り数
dp = [[[0] * 2 for _ in range(N)] for _ in range(K+1)]
dp[0][S][0] = 1
for i in range(K):
    for j in range(N):
        for v in G[j]:
            for k in range(2):
                nk = k if v != X else 1-k
                dp[i+1][v][nk] += dp[i][j][k]
                dp[i+1][v][nk] %= MOD
print(dp[K][T][0]%MOD)

# print(*dp, sep='\n', file=sys.stderr)
