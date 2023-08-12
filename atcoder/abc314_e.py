# https://atcoder.jp/contests/abc314/tasks/abc314_e
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

# 入力
N, M = map(int, input().split())

c, p, s = [], [], []
for i in range(N):
    cps = list(map(int, input().split()))
    c.append(cps[0])
    p.append(cps[1])
    s.append(cps[2:])

# 0ポイントを除き，コストを調整する前処理
for i in range(N):
    c[i] *= p[i]
    s[i] = [i for i in s[i] if i!=0]
    p[i] = len(s[i])
    c[i] /= p[i]

# dp[k] := kポイント残っている時にかかる金額の期待値
dp = [10000 * M] * (M+1)
dp[0] = 0

for k in range(1, M+1):
    for i in range(N):  # ルーレット別にkポイント達成にかかる金額の期待値を計算
        expected = 0    # かかる金額
        for j in range(p[i]):
            dif = k - s[i][j]   # kポイント達成に必要な残りポイント
            if dif <= 0: continue
            expected += dp[dif]                # 残りポイントを達成するまでの期待値
        dp[k] = min(dp[k], c[i] + expected / p[i])    # 期待値が最小のルーレットを選ぶ
for i in range(M+1):
    print(i, dp[i], file=sys.stderr)
print(dp[M])



# https://atcoder.jp/contests/abc314/editorial/6956
# def main():
#     N, M = map(int, input().split())

#     roulette = []
#     for _ in range(N):
#         cps = list(map(int, input().split()))
#         roulette.append([cps[0], cps[1], cps[2:]])

#     # 0 ポイントが出ないように調整
#     for item in roulette:
#         C, P, S = item
#         C *= P
#         S = [s for s in S if s != 0]
#         P = len(S)
#         C /= P
#         item[0], item[1], item[2] = C, P, S

#     e = [10000 * M] * M
#     for i in range(M - 1, -1, -1):  # i の降順に計算
#         for C, P, S in roulette:
#             expected = 0
#             for s in filter(lambda s: i + s < M, S):
#                 expected += e[i + s]  # ルーレットをプレイしたあとにかかる金額の期待値

#             e[i] = min(e[i], C + expected / P)  # C + 1 / P ∑ e[i + s] の最小値が求める e[i]

#     print(e[0])  # e[0] が答え

# if __name__ == "__main__":
#     main()
