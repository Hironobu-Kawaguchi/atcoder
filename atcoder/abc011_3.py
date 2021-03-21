# https://atcoder.jp/contests/abc011/tasks/abc011_3

N = int(input())
NGs = []
for _ in range(3):
    NGs.append(int(input()))

dp = [1000] * (N+1)
dp[-1] = 0

for i in range(N, -1, -1):
    if i not in NGs:
        for j in range(1, 4):
            if i-j >= 0:
                if i-j not in NGs:
                    dp[i-j] = min(dp[i]+1, dp[i-j])

if 1 <= dp[0] <= 100:
    print("YES")
else:
    print("NO")
