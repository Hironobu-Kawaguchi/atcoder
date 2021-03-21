# https://atcoder.jp/contests/abc149/tasks/abc149_c

import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

X = int(input())
while is_prime(X) is False:
    X += 1
print(X)
