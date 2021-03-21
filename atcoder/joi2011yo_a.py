# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_a

t = [int(input()) for _ in range(4)]
div, mod = divmod(sum(t), 60)
print(div)
print(mod)
