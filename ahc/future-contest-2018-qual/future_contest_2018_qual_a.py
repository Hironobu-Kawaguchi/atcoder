# https://atcoder.jp/contests/future-contest-2018-qual/tasks/future_contest_2018_qual_a

import sys
input = sys.stdin.buffer.readline
import math
import random
import time
import numpy as np

# 山登り法の設定
start_time = time.time()
TIME_LIMIT = 5.7

N = 100
Q = 1000
A = np.array([list(map(int, input().split())) for _ in range(N)])

X = [random.randint(0, N - 1) for _ in range(Q)]
Y = [random.randint(0, N - 1) for _ in range(Q)]
H = [1] * Q
B = np.zeros((N * 3, N * 3), dtype=int)
for i in range(Q):
    B[N + Y[i]][N + X[i]] += 1

# H = 1, 2, ..., N に設定された場合の「増減分」を持った numpy 配列を作る
delta = [None] * (N + 1)
for i in range(1, N + 1):
    delta[i] = np.array([[max(i - abs(y) - abs(x), 0) for x in range(-i + 1, i)] for y in range(-i + 1, i)])

# 現在のスコアを取得する関数
def get_score():
    return 200_000_000 - np.absolute(A - B[N:N*2, N:N*2]).sum()

current_score = get_score()

# 山登り法スタート
loops = 0
update_count = 0
while time.time() - start_time < TIME_LIMIT:
    # 「小さな変更」をランダムに選ぶ
    qi = random.randint(0, Q - 1)
    h_limit = 14
    if current_score >= 199900000:
        h_limit = 1
    elif current_score >= 199500000:
        h_limit = 7
    # old_x, new_x = X[qi], X[qi] + random.randint(-9, +9)
    old_x, new_x = X[qi], X[qi] + random.randint(-1, +1)
    # old_y, new_y = Y[qi], Y[qi] + random.randint(-9, +9)
    old_y, new_y = Y[qi], Y[qi] + random.randint(-1, +1)
    # old_h, new_h = H[qi], H[qi] + random.randint(-19, +19)
    old_h, new_h = H[qi], H[qi] + random.randint(-h_limit, +h_limit)
    if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or new_h <= 0 or new_h > N:
        continue

    # X[qi] = new_x, Y[qi] = new_y, H[qi] = new_h に変更（書籍中の Change(qi, new_x, new_y, new_h) の呼び出しに対応）
    B[N + Y[qi] - H[qi] + 1 : N + Y[qi] + H[qi], N + X[qi] - H[qi] + 1 : N + X[qi] + H[qi]] -= delta[H[qi]]
    X[qi], Y[qi], H[qi] = new_x, new_y, new_h
    B[N + Y[qi] - H[qi] + 1 : N + Y[qi] + H[qi], N + X[qi] - H[qi] + 1 : N + X[qi] + H[qi]] += delta[H[qi]]

    # スコアを計算
    new_score = get_score()

    # スコアに応じて採用／不採用を決める
    # 焼きなまし方
    temperature = 180.0 - 179.0 * (time.time() - start_time) / TIME_LIMIT
    # temperature = 190.0 - 189.0 * (time.time() - start_time) / TIME_LIMIT
    # temperature = 220.0 - 200.0 * (time.time() - start_time) / TIME_LIMIT
    probability = math.exp(min((new_score - current_score) / temperature, 0))
    # if current_score < new_score:
    if random.random() < probability:
        current_score = new_score
        update_count += 1
    else:
        # 不採用の場合，oldの値に戻すX
        B[N + Y[qi] - H[qi] + 1 : N + Y[qi] + H[qi], N + X[qi] - H[qi] + 1 : N + X[qi] + H[qi]] -= delta[H[qi]]
        X[qi], Y[qi], H[qi] = old_x, old_y, old_h
        B[N + Y[qi] - H[qi] + 1 : N + Y[qi] + H[qi], N + X[qi] - H[qi] + 1 : N + X[qi] + H[qi]] += delta[H[qi]]
        
    loops += 1

# 出力
print(Q)
for i in range(Q):
    print(X[i], Y[i], H[i])
print(f"Score: {current_score:,.0f}", file=sys.stderr)
print(f"Loops: {loops:,.0f}", file=sys.stderr)
print(f"Update: {update_count:,.0f}", file=sys.stderr)
print(f"Time: {time.time() - start_time:.3f}", file=sys.stderr)
