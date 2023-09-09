# https://atcoder.jp/contests/abc319/tasks/abc319_e

max_d = 840

N, X, Y = map(int, input().split())
P, T = [], []
for _ in range(N-1):
    p, t = map(int, input().split())
    P.append(p)
    T.append(t)
dp = [[0]*(max_d) for _ in range(N)]
for j in range(max_d):
    dp[0][j] = X
for i in range(N-1):
    for j in range(max_d):
        now = dp[i][j] + j
        if now % P[i] == 0:
            mod = 0
        else:
            mod = P[i] - now % P[i]
        dp[i+1][j] = dp[i][j] + mod + T[i]
for j in range(max_d):
    dp[N-1][j] += Y
# for i in range(N):
#     print(dp[i])

Q = int(input())
for qi in range(Q):
    q = int(input())
    div, mod = divmod(q, max_d)
    ans = dp[N-1][mod] + div * max_d + mod
    print(ans)
