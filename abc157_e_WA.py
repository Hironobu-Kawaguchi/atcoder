# https://atcoder.jp/contests/abc157/tasks/abc157_e

import numpy as np
# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input()
nums = np.zeros((26, N+1), dtype=np.int64)
for i in range(1,N+1):
    nums[:,i] = nums[:,i-1]
    c = ord(S[i-1]) - ord('a')
    nums[c,i] = nums[c,i-1] + 1
# print(nums)

Q = int(input())
for i in range(Q):
    t, a, b = input().split()
    if t == '1':
        a = int(a)
        c = ord(S[a-1]) - ord('a')
        nums[c,a:] -= 1
        c = ord(b) - ord('a')
        nums[c,a:] += 1
    else:
        a = int(a)
        b = int(b)
        cnt = np.count_nonzero(nums[:,b] - nums[:,a-1])
        print(cnt)
