# https://atcoder.jp/contests/abc314/tasks/abc314_b
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
lst = []
for i in range(N):
    C = int(input())
    A = set(map(int, input().split()))
    lst.append((i, C, A))
X = int(input())

kake = []
for i in range(N):
    if X in lst[i][2]:
        kake.append((lst[i][1], lst[i][0]+1))
kake.sort()
print(kake, file=sys.stderr)

if len(kake) == 0:
    print(0)
    print()
    exit()

ans = []
nn = kake[0][0]
for c, b in kake:
    if c==nn:
        ans.append(b)

print(len(ans))
print(*ans)
