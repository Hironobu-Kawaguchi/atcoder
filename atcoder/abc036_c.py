# https://atcoder.jp/contests/abc036/tasks/abc036_c

N = int(input())
a, b = [0] * N, [0] * N
for i in range(N):
    a[i] = int(input())
sort_a = sorted(list(set(a)))
d = dict(zip(sort_a, range(len(sort_a))))

for i in range(N):
    b[i] = d[a[i]]

for i in range(N):
    print(b[i])
