# https://atcoder.jp/contests/abc152/tasks/abc152_b

a, b = map(int, input().split())
if a > b:
    print(str(b)*a)
else:
    print(str(a)*b)
