# B - Contest with Drinks Easy
# https://atcoder.jp/contests/abc050/tasks/abc050_b

N = int(input())
T = list(map(int, input().split()))
M = int(input())
P, X = [], []
for i in range(M):
    _p, _x = map(int, input().split())
    P.append(_p)
    X.append(_x)

sm = sum(T)

for i in range(M):
    print(sm + X[i] - T[P[i]-1])
