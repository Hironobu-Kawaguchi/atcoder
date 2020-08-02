# https://atcoder.jp/contests/abc004/tasks/abc004_2

c = []
for i in range(4):
    c.append(list(input().split()))
for i in range(4):
    print(*c[3-i][::-1])
