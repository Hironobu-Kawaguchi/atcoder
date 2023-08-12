# https://atcoder.jp/contests/abc314/tasks/abc314_c
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

s_list = ["" for _ in range(M)]

for i in range(N):
    s_list[C[i]-1] += S[i]
for j in range(M):
    s_list[j] = s_list[j][-1] + s_list[j][:-1]
# print(s_list, file=sys.stderr)

shift_idx = [0] * M
ans = ""
for i in range(N):
    ans += s_list[C[i]-1][shift_idx[C[i]-1]]
    shift_idx[C[i]-1] += 1
print(ans)
