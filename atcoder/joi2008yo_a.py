# A - おつり
# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_a

# おつりの金額
a = 1000 - int(input())

v = [500, 100, 50, 10, 5, 1]
ans = 0

for x in v:
    t = a // x
    a -= t * x
    ans += t

print(ans)
