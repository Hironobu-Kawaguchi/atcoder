# https://atcoder.jp/contests/abc037/tasks/abc037_b

N, Q = map(int, input().split())
a = [0] * N

for i in range(Q):
    L, R, T = map(int, input().split())
    for j in range(L-1, R):
        a[j] = T

for j in range(N):
    print(a[j])
