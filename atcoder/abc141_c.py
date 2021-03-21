# https://atcoder.jp/contests/abc141/tasks/abc141_c

import collections
N, K, Q = map(int, input().split())
A = [int(input())-1 for _ in range(Q)]

c = collections.Counter(A)
# print(c)
for i in range(N):
    if c[i] > Q - K:
        print("Yes")
    else:
        print("No")
