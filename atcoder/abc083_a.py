# https://atcoder.jp/contests/abc083/tasks/abc083_a

a, b, c, d = map(int, input().split())
if a+b > c+d:
    print("Left")
elif a+b == c+d:
    print("Balanced")
else:
    print("Right")
