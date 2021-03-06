# https://atcoder.jp/contests/abc157/tasks/abc157_e

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

import bisect
from string import ascii_lowercase
d = dict()
for i, c in enumerate(ascii_lowercase):
    d[c] = i

N = int(input())
S = list(input())
lst = [[] for _ in range(26)]
for i in range(N):
    lst[d[S[i]]].append(i)

Q = int(input())
for q in range(Q):
    a, b, c = input().split()
    if a=='1':
        i = int(b)-1
        if c == S[i]:   # 変更なし
            continue
        idx = bisect.bisect_left(lst[d[S[i]]],i)
        del lst[d[S[i]]][idx]
        bisect.insort_left(lst[d[c]],i)
        S[i] = c
    else:
        l = int(b)-1
        r = int(c)
        ans = 0
        for i in range(26):
            cnt = bisect.bisect_left(lst[i],r) - bisect.bisect_left(lst[i],l)
            if cnt:
                ans += 1
        print(ans)



# import bisect
# import sys
# def input(): return sys.stdin.readline().rstrip()

# n = int(input())
# s = list(input())
# q = int(input())

# char_idx = [[] for _ in range(26)]
# for i in range(n):
#     char_idx[ord(s[i])-ord('a')].append(i)
# # print(char_idx)

# query = [input().split() for _ in range(q)]
# # print(query)

# for t, a, b in query:
#     if t=='1':
#         i = int(a) - 1
#         if s[i] == b:
#             continue
#         else:
#             idx = bisect.bisect_left(char_idx[ord(s[i])-ord('a')], i)
#             if char_idx[ord(s[i])-ord('a')][idx] == i:
#                 del char_idx[ord(s[i])-ord('a')][idx]
#             bisect.insort_left(char_idx[ord(b)-ord('a')], i)
#             s[i] = b
#     else:
#         l = int(a) - 1
#         r = int(b) - 1
#         ans = 0
#         for i in range(26):
#             if len(char_idx[i]) == 0:
#                 continue
#             it = bisect.bisect_left(char_idx[i], l)
#             if it < len(char_idx[i]) and char_idx[i][it] <= r:
#                 ans += 1
#         print(ans)



# WA
# import numpy as np
# # import sys
# # input = sys.stdin.buffer.readline
# # sys.setrecursionlimit(10 ** 7)

# N = int(input())
# S = input()
# nums = np.zeros((26, N+1), dtype=np.int64)
# for i in range(1,N+1):
#     nums[:,i] = nums[:,i-1]
#     c = ord(S[i-1]) - ord('a')
#     nums[c,i] = nums[c,i-1] + 1
# # print(nums)

# Q = int(input())
# for i in range(Q):
#     t, a, b = input().split()
#     if t == '1':
#         a = int(a)
#         c = ord(S[a-1]) - ord('a')
#         nums[c,a:] -= 1
#         c = ord(b) - ord('a')
#         nums[c,a:] += 1
#     else:
#         a = int(a)
#         b = int(b)
#         cnt = np.count_nonzero(nums[:,b] - nums[:,a-1])
#         print(cnt)
