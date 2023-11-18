# https://atcoder.jp/contests/abc329/tasks/abc329_c

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

from itertools import groupby
N = int(input())
S = input()

cnt = [0] * 26
for c, g in groupby(S):
    i = ord(c) - ord('a')
    cnt[i] = max(cnt[i], len(list(g)))
print(sum(cnt))


# N = int(input())
# S = input()

# cnt = [0] * 26
# now = 1
# cnt[ord(S[0]) - ord('a')] = 1
# for i in range(N-1):
#     j = ord(S[i+1]) - ord('a')
#     if S[i] == S[i+1]:
#         now += 1
#     else:
#         now = 1
#     cnt[j] = max(cnt[j], now)
# ans = sum(cnt)
# print(ans)
