# https://atcoder.jp/contests/abc017/tasks/abc017_3

N, M = map(int, input().split())
imos = [0] * (M+1)
sm = 0
for _ in range(N):
    l, r, s = map(int, input().split())
    imos[l-1] += s
    imos[r] -= s
    sm += s

tmp = 0
dif = sm
for i in range(M):
    tmp += imos[i]
    dif = min(dif, tmp)

print(sm - dif)
