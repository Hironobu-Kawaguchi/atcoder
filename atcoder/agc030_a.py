# A - Poisonous Cookies
# https://atcoder.jp/contests/agc030/tasks/agc030_a

a, b, c = map(int, input().split())
print(b + min(a+b+1, c))
