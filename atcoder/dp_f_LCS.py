# https://atcoder.jp/contests/dp/tasks/dp_f
# pypy
s = input()
t = input()
n = len(s)
m = len(t)
dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

ans = ''
i = n
j = m
while i >= 0 and j >= 0:
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        ans += s[i-1]
        i -= 1
        j -= 1

print(ans[::-1])
