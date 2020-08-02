# https://atcoder.jp/contests/arc012/tasks/

N, va, vb, L = map(int, input().split())

for i in range(N):
    L = L *vb / va

print("{:.12f}".format(L))
