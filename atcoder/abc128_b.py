# B - Guidebook
# https://atcoder.jp/contests/abc128/tasks/abc128_b

N = int(input())
sp = []

for i in range(N):
    s, p = input().split()
    sp.append([s, -int(p), i])
sp.sort()

for i in range(N):
    print(sp[i][2]+1)
