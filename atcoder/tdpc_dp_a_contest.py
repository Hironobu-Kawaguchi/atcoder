# https://atcoder.jp/contests/tdpc/tasks/tdpc_contest

import sys
input = sys.stdin.buffer.readline

N = int(input())
p = list(map(int, input().split()))

s = set([0])
for y in p:
    s |= set(x+y for x in s)
print(len(s))
