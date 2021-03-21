# https://atcoder.jp/contests/abc096/tasks/abc096_a

a, b = map(int, input().split())

if a <= b:
    ans = a
else:
    ans = a - 1

print(ans)
