# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_a

X, Y = map(int, input().split())

d = {1:300000, 2:200000, 3:100000}

ans = 0
if X in d:
    ans += d[X]
if Y in d:
    ans += d[Y]
if X == Y == 1:
    ans += 400000

print(ans)
