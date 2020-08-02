# https://atcoder.jp/contests/abc158/tasks/abc158_c

import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

A, B = map(int, input().split())
ans = -1
for x in range(1100):
    if int(x*0.08) == A and int(x*0.10) == B:
        ans = x
        break

print(ans)
