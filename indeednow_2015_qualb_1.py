# https://atcoder.jp/contests/indeednow-qualb/tasks/indeednow_2015_qualb_1

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
ans = abs(x1-x2) + abs(y1-y2) + 1
print(ans)
