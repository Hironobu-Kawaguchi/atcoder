# https://atcoder.jp/contests/abc326/tasks/abc326_c

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
for i in range(N):
    x = A[i]
    j = bisect.bisect_left(A, x + M)
    ans = max(ans, j - i)
    # print(i, j, j - i, ans)
print(ans)
