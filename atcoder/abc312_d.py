# https://atcoder.jp/contests/abc312/tasks/abc312_d

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
MOD = 998244353

S = input()
N = len(S)
MaxDiff = 1501

dp = [[0] * MaxDiff for _ in range(N+1)]   # dp[i][j] i:チェックしたSのindex, j:"("の数 - ")"の数
dp[0][0] = 1

for i in range(N):
    if S[i]=='(':  # "("の場合
        for j in range(MaxDiff-1):
            dp[i+1][j+1] = dp[i][j]
    elif S[i]==')': # ")"の場合
        for j in range(MaxDiff-1):
            dp[i+1][j] = dp[i][j+1]
    elif S[i]=='?':
        # '('を追加する場合
        for j in range(MaxDiff-1):
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= MOD
        # ')'を追加する場合
        for j in range(MaxDiff-1):
            dp[i+1][j] += dp[i][j+1]
            dp[i+1][j] %= MOD
print(dp[N][0])
