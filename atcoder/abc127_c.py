# C - Prison
# https://atcoder.jp/contests/abc127/tasks/abc127_c

N, M = map(int, input().split())

lmax = 0
rmin = N
for i in range(M):
    L, R = map(int, input().split())
    lmax = max(L, lmax)
    rmin = min(R, rmin)

ans = max(rmin - lmax + 1, 0)
print(ans)

