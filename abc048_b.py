# B - Between a and b ...
# https://atcoder.jp/contests/abc048/tasks/abc048_b

a, b, x = map(int, input().split())
if a % x == 0:
    print(b//x - a//x + 1)
else:
    print(b//x - a//x)
    