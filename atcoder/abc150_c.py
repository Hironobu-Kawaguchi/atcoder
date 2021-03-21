# https://atcoder.jp/contests/abc150/tasks/abc150_c

import itertools
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

for i, lst in enumerate(itertools.permutations(range(1,N+1))):
    if lst == P:
        p = i
    if lst == Q:
        q = i
print(abs(p-q))
