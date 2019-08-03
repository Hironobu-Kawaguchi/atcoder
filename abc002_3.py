# https://atcoder.jp/contests/abc002/tasks/abc002_3

xa, ya, xb, yb, xc, yc = map(int, input().split())
ans = abs((xb-xa)*(yc-ya) - (xc-xa)*(yb-ya)) / 2
print(ans)
