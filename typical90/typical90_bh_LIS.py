# https://atcoder.jp/contests/typical90/tasks/typical90_bh

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import bisect

# Step #1. 入力
N = int(input())
A = list(map(int, (input().split())))

# Step #2. 左側の LIS を求める
P = [-1]*N
dp = [-1]*N
cnt = 0
for i in range(N):
    pos = bisect.bisect_left(dp, A[i], 0, cnt)
    dp[pos] = A[i]
    P[i] = pos + 1
    if pos==cnt:
        cnt += 1
# print(P)
# print(cnt, dp[:cnt])

# Step #3. 右側の LIS を求める
Q = [-1]*N
dp = [-1]*N
cnt = 0
for i in range(N-1, -1, -1):
    pos = bisect.bisect_left(dp, A[i], 0, cnt)
    dp[pos] = A[i]
    Q[i] = pos + 1
    if pos==cnt:
        cnt += 1
# print(Q)
# print(cnt, dp[:cnt])

# Step #4. 答えを求める
ans = 0
for i in range(N):
    ans = max(ans, P[i] + Q[i] - 1)
print(ans)
