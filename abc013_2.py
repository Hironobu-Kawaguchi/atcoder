# https://atcoder.jp/contests/abc013/tasks/abc013_2

a = int(input())
b = int(input())
ans = min(abs(a-b), 10 - abs(a-b))
print(ans)
