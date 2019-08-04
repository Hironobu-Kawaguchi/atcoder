# https://atcoder.jp/contests/abc136/tasks/abc136_a

A, B, C = map(int, input().split())

ans = C - min((A - B), C)
print(ans)
