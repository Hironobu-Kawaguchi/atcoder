# https://atcoder.jp/contests/abc014/tasks/abc014_1

a = int(input())
b = int(input())

if a % b:
    ans = b - a % b
else:
    ans = 0
print(ans)
