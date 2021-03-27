# https://atcoder.jp/contests/abc197/tasks/abc197_d

N = int(input())
Cs = [[] for _ in range(N)]
for i in range(N):
    x, c = map(int, input().split())
    Cs[c-1].append(x)
for i in range(N):
    Cs[i].sort()
minmax = [[0,0]]
for i in range(N):
    if len(Cs[i])==0: continue
    minmax.append([Cs[i][0], Cs[i][-1]])
minmax.append([0,0])
# print(minmax)
dp = [[0,0] for _ in range(len(minmax))]
for i in range(len(minmax)-1):
    dp[i+1][0] = min(dp[i][0] + abs(minmax[i+1][1] - minmax[i][0]) + abs(minmax[i+1][0] - minmax[i+1][1])
                    ,dp[i][1] + abs(minmax[i+1][1] - minmax[i][1]) + abs(minmax[i+1][0] - minmax[i+1][1]))
    dp[i+1][1] = min(dp[i][0] + abs(minmax[i+1][0] - minmax[i][0]) + abs(minmax[i+1][0] - minmax[i+1][1])
                    ,dp[i][1] + abs(minmax[i+1][0] - minmax[i][1]) + abs(minmax[i+1][0] - minmax[i+1][1]))
# print(dp)
print(dp[-1][0])

