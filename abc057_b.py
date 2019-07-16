# B - Checkpoints
# https://atcoder.jp/contests/abc057/tasks/abc057_b

N, M = map(int, input().split())
a, b = [], []
for i in range(N):
    _a, _b = map(int, input().split())
    a.append(_a)
    b.append(_b)
c, d = [], []
for j in range(M):
    _c, _d = map(int, input().split())
    c.append(_c)
    d.append(_d)

for i in range(N):
    ans = 10 ** 9
    for j in range(M):
        tmp = abs(a[i]-c[j]) + abs(b[i]-d[j])
        if tmp < ans:
            ans = tmp
            jj = j
    print(jj + 1)
