# https://atcoder.jp/contests/arc051/tasks/arc051_b

k = int(input())
f = [1, 1]
for i in range(k-1):
    f.append(f[-1]+f[-2])
print(f[-2], f[-1])
