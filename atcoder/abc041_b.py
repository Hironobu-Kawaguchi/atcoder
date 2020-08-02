# https://atcoder.jp/contests/abc041/tasks/abc041_b

A, B, C = map(int, input().split())
mod = 10 ** 9 + 7
ans = A * B * C % mod
print(ans)
