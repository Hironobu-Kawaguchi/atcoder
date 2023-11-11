# https://atcoder.jp/contests/abc323/tasks/abc323_e
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

MOD = 998244353

N, X = map(int, input().split())
T = list(map(int, input().split()))
N_inv = pow(N, MOD - 2, MOD)

dp = [0] * (X+1)        # dp[i]: i秒の時の曲1が再生されている確率
for i in range(X+1):
    for j in range(N):
        if T[j] > i:    # まだ1曲目が終わっていない場合，j=0の時だけ曲1が再生されている
            dp[i] += 1 if j == 0 else 0
        else:
            dp[i] += dp[i - T[j]]   # 1曲目が終わっている場合，終わった時からのdp
    dp[i] = dp[i] * N_inv % MOD     # Nで割る
print(dp[X])
