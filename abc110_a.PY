# A - Maximize the Formula
# https://atcoder.jp/contests/abc110/tasks/abc110_a

Nums = list(map(int, input().split()))
ans = max(Nums) * 9 + sum(Nums)

print(ans)