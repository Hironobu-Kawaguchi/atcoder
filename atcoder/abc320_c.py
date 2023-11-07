# https://atcoder.jp/contests/abc320/tasks/abc320_c
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

from itertools import permutations
INF = 10 ** 18

M = int(input())
S = [input() for _ in range(3)]
idx = [[[] for _ in range(10)] for _ in range(3)]

for i in range(3):
    for j in range(M):
        idx[i][int(S[i][j])].append(j)
# print(idx)

ans = INF
for it in permutations(range(3), 3):
    # print(it)
    for i in range(10):
        if len(idx[0][i]) == 0 or len(idx[1][i]) == 0 or len(idx[2][i]) == 0:
            continue
        t = 0
        for ii, j in enumerate(it):
            if ii>0: t += 1
            for k in range(len(idx[j][i])):
                if idx[j][i][k] >= t%M:
                    t += idx[j][i][k] - t%M
                    break
            else:
                t += idx[j][i][0] + M - t%M
        ans = min(ans, t)

if ans == INF:
    print(-1)
else:
    print(ans)
