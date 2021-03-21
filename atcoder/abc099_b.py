# https://atcoder.jp/contests/abc099/tasks/abc099_b

a, b = map(int, input().split())

n = b - a
ans = sum(range(n)) - a

print(ans)
