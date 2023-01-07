# https://atcoder.jp/contests/typical90/tasks/typical90_aj
import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
INF = 1001001001

N, Q = map(int, input().split())
x_max, x_min = -INF, INF
y_max, y_min = -INF, INF
X = [0] * N
Y = [0] * N
for i in range(N):
    _x, _y = map(int, input().split())
    X[i] = _x - _y
    Y[i] = _x + _y
    x_max = max(x_max, X[i])
    x_min = min(x_min, X[i])
    y_max = max(y_max, Y[i])
    y_min = min(y_min, Y[i])

for i in range(Q):
    q = int(input())
    ans = max(abs(X[q-1] - x_min), abs(X[q-1] - x_max), abs(Y[q-1] - y_min), abs(Y[q-1] - y_max))
    print(ans)
