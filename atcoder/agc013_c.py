# C - Ants on a Circle
# https://agc013.contest.atcoder.jp/tasks/agc013_c
N, L, T = map(int, input().split())

s = 0
X = [0] * N
for i in range(N):
    x, w = map(int, input().split())
    x += ((w + 1) % 3 - 1) * T
    # xが0点を通る回数を足す
    s += x // L
    X[i] = x % L

X.sort()
for i in range(N):
    print(X[(i+s) % N])
