# https://atcoder.jp/contests/abc318/tasks/abc318_d
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
# D = [list(map(int, input().split())) for _ in range(N)]
D = [[-1]*N for _ in range(N)]
for i in range(N):
    _d = list(map(int, input().split()))
    for j in range(N-i-1):
        D[i][i+j+1] = _d[j]
        D[i+j+1][i] = _d[j]
# print(D, file=sys.stderr)

# dp[S]は、頂点集合Sが既にマッチングされているときの最大重みの合計を表す
dp = [-1] * (1 << N)
dp[0] = 0
# print(dp, file=sys.stderr)

for S in range(1 << N):
    # Sに含まれる頂点の数が奇数なら、このような集合に対するマッチングは存在しない
    if bin(S).count("1") % 2 == 1:
        continue

    for i in range(N):
        for j in range(i + 1, N):
            # 両方の点がSに含まれていなければスキップ
            if not ((S >> i) & 1) or not ((S >> j) & 1):
                continue

            # dp[S]を更新
            T = S ^ (1 << i) ^ (1 << j)  # Sからiとjを除いた集合
            if dp[T] == -1:
                continue
            # print(S, T, file=sys.stderr)
            dp[S] = max(dp[S], dp[T] + D[i][j])
# print(dp, file=sys.stderr)

# print(dp[-1])
ans = -1
for i in range(1 << N):
    ans = max(ans, dp[i])
print(ans)
