# https://atcoder.jp/contests/abc066/tasks/abc066_a

a, b, c = map(int, input().split())
ans = a + b + c - max(a, max(b, c))
print(ans)
