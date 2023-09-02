# https://atcoder.jp/contests/abc317/tasks/abc317_d

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
INF = 1001001001001

N = int(input())
takahashi = []
aoki = []
takahashi_sum, aoki_sum = 0, 0
for _ in range(N):
    x, y, z = map(int, input().split())
    if x>y:
        takahashi.append((z, (x-y+1)//2))
        takahashi_sum += z
    elif x<y:
        aoki.append((z, (y-x+1)//2))
        aoki_sum += z
dif = (aoki_sum - takahashi_sum + 1) // 2
# print(dif, takahashi_sum, aoki_sum, file=sys.stderr)
# print(aoki, file=sys.stderr)

if dif < 0:
    print(0)
    exit()

dp = [INF] * (dif+1)
dp[0] = 0
for z, d in aoki:
    for i in range(dif, -1, -1):
        if dp[i] == INF: continue
        j = min(i+z, dif)
        dp[j] = min(dp[j], dp[i] + d)
print(dp[dif])
# print(dp, file=sys.stderr)
