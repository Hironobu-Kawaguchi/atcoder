# https://atcoder.jp/contests/typical90/tasks/typical90_br

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
# sumX, sumY = 0, 0
X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    # sumX += x
    # sumY += y
# meanX = sumX / N
# meanX = (sumX+N-1) // N
# meanY = sumY / N
# meanY = (sumY+N-1) // N
# print(sumX, sumY, meanX, meanY)
X.sort()
Y.sort()
midX = X[N//2]
midY = Y[N//2]

ans = 0
for i in range(N):
    ans += abs(X[i] - midX) + abs(Y[i] - midY)

print(ans)
