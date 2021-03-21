# https://atcoder.jp/contests/abc145/tasks/abc145_c

N = int(input())
x, y = [], []
for i in range(N):
    _x, _y = map(int, input().split())
    x.append(_x)
    y.append(_y)

sums = 0
for i in range(N-1):
    for j in range(i+1, N):
        sums += ((x[i]-x[j])**2 + (y[i]-y[j])**2)**0.5

ans = sums * (N-1) / (N*(N-1)/2)
print(ans)
