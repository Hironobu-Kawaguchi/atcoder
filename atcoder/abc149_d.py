# https://atcoder.jp/contests/abc149/tasks/abc149_d

d = {'r': 0, 's': 1, 'p': 2}
win = {0: 2, 1: 0, 2: 1}

N, K = map(int, input().split())
point = list(map(int, input().split()))
T = input()

dp = [[0]*3 for _ in range(K)]  # K周期で最後に出した手別の最大得点

for i in range(N):
    k = i%K
    w = win[d[T[i]]]
    mx, mxw = 0, 0
    for j in range(3):
        mx = max(mx, dp[k][j])
        if j != w:
            mxw = max(mxw, dp[k][j])
    for j in range(3):
        if j != w:
            dp[k][j] = mx   # 今回は負けるので前回のmax
        else:
            dp[k][j] = mxw + point[j]   # 今回勝つので、前回別の手のmax + point[j]

ans = 0
for i in range(K):
    mx = 0
    for j in range(3):
        mx = max(mx, dp[i][j])
    ans += mx

# print(dp)
print(ans)
