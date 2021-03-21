# https://atcoder.jp/contests/abc159/tasks/abc159_f
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
MOD = 998244353

N, S = map(int, input().split())
A = list(map(int, list(input().split())))

ans = 0
dp = [0]*(S+1)
for i in range(N):
    dp[0] += 1      # Lがiからを足す
    next_dp = [0]*(S+1)
    for j in range(S+1):
        next_dp[j] += dp[j]             # A[i]を選ばない
        next_dp[j] %= MOD
        if j+A[i]<=S:
            next_dp[j+A[i]] += dp[j]    # A[i]を選ぶ
            next_dp[j+A[i]] %= MOD
    dp = next_dp
    ans += dp[S]    # Rがiまでを足す
    ans %= MOD

print(ans)


# N, S = map(int, input().split())
# A = list(map(int, list(input().split())))

# ans = 0
# dp = [[0]*(S+1) for _ in range(N+1)]
# for i in range(N):
#     dp[i][0] += 1       # Lがiからを足す
#     for j in range(S+1):
#         dp[i+1][j] += dp[i][j]             # A[i]を選ばない
#         dp[i+1][j] %= MOD
#         if j+A[i]<=S:
#             dp[i+1][j+A[i]] += dp[i][j]    # A[i]を選ぶ
#             dp[i+1][j+A[i]] %= MOD
#     ans += dp[i+1][S]    # Rがiまでを足す
#     ans %= MOD

# print(ans)
