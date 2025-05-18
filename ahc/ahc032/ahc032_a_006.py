# https://atcoder.jp/contests/ahc032/tasks/ahc032_a

import sys
import time
import random
import math
# import copy
sys.setrecursionlimit(10 ** 7)
MOD = 998244353

# 時間を記録
start_time = time.time()

N, M, K = map(int, input().split()) # N=9: マス目の大きさ, M=20: スタンプの数, K=81: 最大ターン数
A = [list(map(int, input().split())) for _ in range(N)]
# print(*A, file=sys.stderr)
S = [[list(map(int, input().split())) for _ in range(3)]for _ in range(M)]
# print(*S, file=sys.stderr)

def calc_score(a):
    score = 0
    for i in range(N):
        for j in range(N):
            score += a[i][j] % MOD
    return score

def calc_score_diff_add(a, m, p, q):
    score_diff = 0
    for i in range(3):
        for j in range(3):
            score_diff += S[m][i][j]
            if a[p+i][q+j] + S[m][i][j] >= MOD:
                score_diff -= MOD
    return score_diff

def stamp_add(a, m, p, q):
    for i in range(3):
        for j in range(3):
            a[p+i][q+j] += S[m][i][j]
            a[p+i][q+j] %= MOD
    return a

def calc_score_diff_remove(a, idx):
    score_diff = 0
    m, p, q = ans[idx]
    for i in range(3):
        for j in range(3):
            score_diff -= S[m][i][j]
            if a[p+i][q+j] - S[m][i][j] < 0:
                score_diff += MOD
    return score_diff

def stamp_remove(a, idx):
    m, p, q = ans[idx]
    for i in range(3):
        for j in range(3):
            a[p+i][q+j] -= S[m][i][j]
            a[p+i][q+j] += MOD
            a[p+i][q+j] %= MOD
    return a

def calc_score_diff_change(a, idx, m, p, q):
    m_old, p_old, q_old = ans[idx]
    # 場所の重複を考慮
    A_diff = [[0]*N for _ in range(N)]
    for i in range(3):
        for j in range(3):
            A_diff[p_old+i][q_old+j] -= S[m_old][i][j]
            A_diff[p+i][q+j] += S[m][i][j]
    score_diff = 0
    for i in range(N):
        for j in range(N):
            score_diff += A_diff[i][j]
            if a[i][j] + A_diff[i][j] >= MOD:
                score_diff -= MOD
            elif a[i][j] + A_diff[i][j] < 0:
                score_diff += MOD
    return score_diff

def stamp_change(a, idx, m, p, q):
    m_old, p_old, q_old = ans[idx]
    for i in range(3):
        for j in range(3):
            a[p_old+i][q_old+j] -= S[m_old][i][j]
            a[p_old+i][q_old+j] += MOD
            a[p_old+i][q_old+j] %= MOD
            a[p+i][q+j] += S[m][i][j]
            a[p+i][q+j] %= MOD
    return a

def print_iter_score():
    if iter % 10000 == 0:
        print(f"iter:{iter:0>8}, score: {score}", file=sys.stderr)
    return

ans = []
score = calc_score(A)

iter = 0
iter_select = 0
print_iter_score()
# 焼きなまし法
NUM_LOOPS = 400000

# while time.time() - start_time < 1.5:
while iter < NUM_LOOPS:
    type = True     # True: 追加, False: 交換
    # if len(ans) == K: break
    if len(ans) == 0:
    # if len(ans) < K:
        type = True
    elif len(ans) == K:
        type = False
    else:
        type = random.choice([True, False])
    T = 3*1e8 - 3*1e8 * (iter / NUM_LOOPS)
    if T < 1: T = 1     # 0除算回避
    if type:
        m = random.randint(0, M-1)
        p = random.randint(0, N-3)
        q = random.randint(0, N-3)
        score_diff = calc_score_diff_add(A, m, p, q)
        probability = math.exp(min(score_diff / T, 0))
        if random.random() < probability:
        # if score_diff > 0:
            A = stamp_add(A, m, p, q)
            ans.append([m, p, q])
            score += score_diff
            # score = calc_score(A)
            iter_select += 1
    else:
        idx = random.randint(0, len(ans)-1)
        m = random.randint(0, M-1)
        p = random.randint(0, N-3)
        q = random.randint(0, N-3)
        score_diff = calc_score_diff_change(A, idx, m, p, q)
        probability = math.exp(min(score_diff / T, 0))
        if random.random() < probability:
        # if score_diff > 0:
            A = stamp_change(A, idx, m, p, q)
            ans[idx] = [m, p, q]
            score += score_diff
            # score = calc_score(A)
            iter_select += 1
    # else:
    #     idx = random.randint(0, len(ans)-1)
    #     score_diff = calc_score_diff_remove(A, idx)
    #     if score_diff > 0:
    #         A = stamp_remove(A, idx)
    #         score += score_diff
    #         ans.pop(idx)
    iter += 1
    print_iter_score()

print(len(ans))
for m, p, q in ans:
    print(m, p, q)

print("L:", len(ans), "iter:", iter, "selected iter:", iter_select, file=sys.stderr)
print("final score:", score, file=sys.stderr)
print("score check:", calc_score(A), file=sys.stderr)
print("elapsed_time:", time.time() - start_time, file=sys.stderr)
for i in range(N):
    for j in range(N):
        assert A[i][j] < MOD
