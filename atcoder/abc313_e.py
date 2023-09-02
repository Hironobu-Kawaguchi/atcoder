# https://atcoder.jp/contests/abc313/tasks/abc313_e
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
MOD =998244353

N = int(input())
S = input()

def solve():
    for i in range(N-1):
        if S[i]!='1' and S[i+1]!='1':
            # print(i, S[i], S[i+1], file=sys.stderr)
            print(-1)
            return
    dp = [0]*N
    dp[N-1] = 1
    for i in range(N-2, -1, -1):
        n = int(S[i+1])
        dp[i] = dp[i+1] + dp[i+1] * (n-1) + 1
        dp[i] %= MOD
    # print(*dp, file=sys.stderr)
    print((dp[0] + MOD - 1)%MOD)
    return

solve()
