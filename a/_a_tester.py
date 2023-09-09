# https://atcoder.jp/contests/abc313/tasks/abc313_d

import sys
import random

N, K = 10, 5
print(N, K)
# print(N, K, file=sys.stderr)
A = [random.randint(0, 1) for _ in range(N)]
print(*A, file=sys.stderr)

while True:
    line = input()
    c, x = line[0], line[2:]
    x = list(map(int, x.split()))
    if c=="?":
        res = 0
        for i in x:
            res ^= A[i-1]
        print(res)
    else:
        assert x == A, "Wrong Answer"
        break
