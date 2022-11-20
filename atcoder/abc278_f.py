# https://atcoder.jp/contests/abc278/tasks/abc278_f

import sys
# input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
S = [input() for _ in range(N)]
# print(S)
n2 = 1<<N

mem = [[False] * N for _ in range(n2)]
val = [[False] * N for _ in range(n2)]

def f(s, p):
    if mem[s][p]: return val[s][p]
    res = False
    for i in range(N):
        if (s>>i&1): continue
        if (s and S[i][0]!=S[p][-1]): continue
        res |= not f(s|1<<i,i)
    mem[s][p] = True
    val[s][p] = res
    return res

if f(0,0):
    print("First")
else:
    print("Second")
