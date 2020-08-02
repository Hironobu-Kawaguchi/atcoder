# https://atcoder.jp/contests/abc064/tasks/abc064_a

r, g, b = input().split()
rgb = int(r + g + b)
if rgb % 4 == 0:
    print("YES")
else:
    print("NO")
