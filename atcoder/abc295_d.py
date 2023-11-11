# https://atcoder.jp/contests/abc295/tasks/abc295_d
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)


S = input()

cnt = [0] * (1<<10)
cnt[0] = 1
now = 0
ans = 0
for i in range(len(S)):
    now ^= (1<<int(S[i]))
    ans += cnt[now]
    cnt[now] += 1
print(ans)


# S = input()

# cnt = [0] * (1<<10)
# cnt[0] = 1
# now = 0
# for i in range(len(S)):
#     now ^= (1<<int(S[i]))
#     cnt[now] += 1
# ans = 0
# for i in range(1<<10):
#     ans += cnt[i] * (cnt[i]-1) // 2
# print(ans)



# S = input()

# cumcnt = [[0]*10 for _ in range(len(S)+1)]
# for i in range(len(S)):
#     for j in range(10):
#         cumcnt[i+1][j] = cumcnt[i][j]
#     cumcnt[i+1][int(S[i])] += 1
# print(cumcnt, file=sys.stderr)


# ans = 0
# for l in range(len(S)-1):
#     for r in range(l+1, len(S)):
#         flg = True
#         for i in range(10):
#             if (cumcnt[r+1][i] - cumcnt[l][i]) % 2:
#                 flg = False
#                 break
#         if flg:
#             ans += 1
#             print(l+1, r+1, file=sys.stderr)
# print(ans)
