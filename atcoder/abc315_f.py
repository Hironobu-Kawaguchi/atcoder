# https://atcoder.jp/contests/abc315/tasks/abc315_f
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
import math
INF = 10**18

N = int(input())
CheckPoint = []
for i in range(N):
    x, y = map(int, input().split())
    CheckPoint.append((x, y))

def dist(i, j):
    x1, y1 = CheckPoint[i]
    x2, y2 = CheckPoint[j]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# max_c = min(N - 2, 60)
# max_c = min(N, 60)
max_c = 20
dp = [[INF] * (max_c + 1) for _ in range(N)]    # dp[i][k] i:スルーした最後のチェックポイント, k:スルーした回数
dp[0][0] = 0
for i in range(1, N):   # 現在のチェックポイント
    for j in range(i-1, max(-1, i-max_c-5), -1):    # スルーした最後のチェックポイント
        skip = i - j - 1    # いくつ前のチェックポイントから移動するか, j=i-1の時はskip=0
        for k in range(max_c - skip):
            dp[i][k + skip] = min(dp[i][k + skip], dp[j][k] + dist(j, i))

ans = INF
for c in range(max_c + 1):
    if dp[N-1][c] == INF: continue
    if c == 0:
        penalty = 0
    else:
        penalty = 2**(c-1)
    ans = min(ans, dp[N-1][c] + penalty)
print(ans)




# https://atcoder.jp/contests/abc315/editorial/6993
# import sys
# import math
# from typing import List, Tuple

# # 距離を計算する関数
# def dist(a: Tuple[int, int], b: Tuple[int, int]) -> float:
#     dx = a[0] - b[0]
#     dy = a[1] - b[1]
#     ss = dx * dx + dy * dy
#     return math.sqrt(ss)

# def main():
#     # 入力
#     n = int(input())
#     vp = [tuple(map(int, input().split())) for _ in range(n)]

#     # 距離の上限値を設定
#     lg = 8.0e18

#     # dpテーブルの初期化
#     dp = [[lg] * 60 for _ in range(n)]
#     dp[0][0] = 0.0

#     # dpテーブルの更新
#     for i in range(1, n):
#         for j in range(i-1, -1, -1):
#             skip = i - j - 1
#             for k in range(60 - skip):
#                 dp[i][k + skip] = min(dp[i][k + skip], dp[j][k] + dist(vp[j], vp[i]))

#     # ペナルティを考慮して最小のコストを求める
#     res = lg
#     for i in range(60):
#         pen = 0.0
#         if i > 0:
#             pen = 2.0 ** (i - 1)
#         res = min(res, dp[n-1][i] + pen)

#     # 結果の出力
#     print(f"{res:.6f}")

# if __name__ == "__main__":
#     main()
