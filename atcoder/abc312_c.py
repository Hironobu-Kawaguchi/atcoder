# https://atcoder.jp/contests/abc312/tasks/abc312_c

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))
B.sort()
C = A + B
C.sort()

for i, c in enumerate(C):
    for j in range(2):
        x = c + j
        cnt_sell = bisect.bisect_right(A, x)
        cnt_buy = M - bisect.bisect_left(B, x)
        print(x, cnt_sell, cnt_buy, file=sys.stderr)
        if cnt_sell >= cnt_buy:
            print(x)
            exit()

