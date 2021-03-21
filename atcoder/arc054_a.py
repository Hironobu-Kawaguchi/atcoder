# https://atcoder.jp/contests/arc054/tasks/arc054_a

L, X, Y, S, D = map(int, input().split())
if S <= D:
    r = D - S
    l = S + (L-D)
else:
    r = (L-S) + D
    l = S - D

if Y > X:
    ans = min(r/(X+Y), l/(Y-X))
else:
    ans = r/(X+Y)

print(ans)
