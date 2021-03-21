# https://atcoder.jp/contests/abc061/tasks/abc061_c

N, K = map(int, input().split())
l = []
for i in range(N):
    a, b = map(int, input().split())
    l.append([a, b])
l.sort()

num = 0
for i in range(N):
    num += l[i][1]
    if num >= K:
        print(l[i][0])
        break
