# https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_d

INF = 10e15
N, M = map(int, input().split())
LRC = [tuple(map(int, input().split())) for _ in range(M)]
LRC.sort()
# print(LRC)

dp = [INF] * N
dp[0] = 0

for l, r, c in LRC:
    l -= 1
    r -= 1
    # print(l, r, c)
    if dp[l] == INF:
        continue
    for i in range(r, l, -1):
        if dp[i] > dp[l] + c:
            dp[i] = dp[l] + c
        else:
            break

# print(dp)
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
