# https://atcoder.jp/contests/abc196/tasks/abc196_e

INF = 1001001001
N = int(input())
A, T = [0]*N, [0]*N
for i in range(N):
    A[i], T[i] = map(int, input().split())
# print(a, t)
t1 = 0
t2 = -INF
t3 = INF
for i in range(N):
    if T[i]==1:     # +
        t1 += A[i]
    elif T[i]==2:   # max
        t2 = max(t2, A[i]-t1)
    else:           # min
        t3 = min(t3, A[i]-t1)
        t2 = min(t2, A[i]-t1)
# print(t1, t2, t3)

Q = int(input())
X = list(map(int, (input().split())))
# print(X)
for x in X:
    ans = t1 + max(t2, min(t3, x))
    print(ans)
