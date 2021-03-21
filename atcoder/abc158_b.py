# https://atcoder.jp/contests/abc158/tasks/abc158_b

import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

N, A, B = map(int, input().split())

div, mod = divmod(N, A+B)
ans = div * A + min(mod, A)

print(ans)
