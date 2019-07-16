# C - /\/\/\/
# https://atcoder.jp/contests/abc111/tasks/arc103_a

import numpy as np
even = np.zeros(100001, dtype=int)
odd = np.zeros(100001, dtype=int)

n = int(input())
v = list(map(int, input().split()))

for i in range(n):
    if i % 2 == 0:
        even[v[i]] += 1
    else:
        odd[v[i]] += 1

e1 = even.argmax()
e1n = even.max()
o1 = odd.argmax()
o1n = odd.max()

# print(e1, e1n, o1, o1n)
if e1 == o1:
    e2n = np.sort(even)[-2]
    o2n = np.sort(odd)[-2]
    # print(e2n, o2n)
    print(min(n - e1n - o2n, n - e2n - o1n))
else:
    print(n - e1n - o1n)
