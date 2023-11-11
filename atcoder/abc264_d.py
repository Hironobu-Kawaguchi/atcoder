# https://atcoder.jp/contests/abc264/tasks/abc264_d
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

d = {k:v for k, v in zip("atcoder", range(7))}
# print(d)

S = input()
# 転倒数
ans = 0
for i in range(len(S)):
    for j in range(i+1, len(S)):
        if d[S[i]] > d[S[j]]:
            ans += 1
print(ans)
