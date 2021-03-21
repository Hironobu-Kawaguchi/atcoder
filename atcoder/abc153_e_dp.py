# https://atcoder.jp/contests/abc153/tasks/abc153_e

INF = 1001001001
H, N = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
dp = [INF] * (20000)
dp[0] = 0
for a,b in ab:
    for j in range(H):
        if dp[j+a] > dp[j] + b:
            dp[j+a] = dp[j] + b
print(min(dp[H:]))


# INF = 1001001001
# H, N = map(int, input().split())
# ab = [list(map(int, input().split())) for _ in range(N)]
# dp = [INF] * (H+1)
# dp[0] = 0
# for i in range(N):
#     for j in range(H+1):
#         if j>ab[i][0]:
#             dp[j] = min(dp[j], dp[j-ab[i][0]] + ab[i][1])
#         else:
#             dp[j] = min(dp[j], ab[i][1])
# print(dp[H])
