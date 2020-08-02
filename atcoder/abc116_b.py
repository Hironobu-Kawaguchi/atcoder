# B - Collatz Problem
# https://atcoder.jp/contests/abc116/tasks/abc116_b

s = int(input())
a = [s]

def f(n):
    if n % 2 == 0:
        return n //2
    else:
        return 3 * n + 1

for i in range(1000000):
    an = f(a[i])
    if an in a:
        m = i + 2
        break
    else:
        a.append(an)

print(m)
# print(a)
