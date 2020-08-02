# G - ますまてぃくす・おりんぴっく！
# https://atcoder.jp/contests/iroha2019-day3/tasks/iroha2019_day3_g

import itertools

def f2():
    # d = b**2 - 4 * a * (c-2019) > 0
    res = 0
    for a, b, c in itertools.product(range(10**2), repeat=3):
        # print(a,b,c)
        if b**2 - 4 * a * (c-2019) > 0:
            res += 1
    return res

n = input()

if n == '0':
    print(1+4)
elif n == '1':
    print(5)
elif n == '2':
    # print(999999990000)
    print(f2())
elif n == '3':
    print()
elif n == '4':
    print()
elif n == '5':
    print()

