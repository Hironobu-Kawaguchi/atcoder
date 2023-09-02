# https://atcoder.jp/contests/abc317/tasks/abc317_a

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, H, X = map(int, input().split())
P = list(map(int, input().split()))

for i in range(N):
    if H + P[i] >= X:
        print(i+1)
        exit()
