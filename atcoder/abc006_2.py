# https://atcoder.jp/contests/abc006/tasks/abc006_2

n = int(input())
DP = [0] * n
if n <= 2:
    ans = 0
elif n == 3:
    ans = 1
else:
    DP[0] = 0
    DP[1] = 0
    DP[2] = 1
    for i in range(3, n):
        DP[i] = (DP[i-1] + DP[i-2] + DP[i-3]) % 10007
    ans = DP[n-1]
print(ans)
