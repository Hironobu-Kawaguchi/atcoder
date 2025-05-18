# https://atcoder.jp/contests/ahc028/tasks/ahc028_a
from dataclasses import dataclass
from enum import Enum
import sys
import copy
# from collections import deque
# from itertools import permutations
# import heapq
sys.setrecursionlimit(1000000)
# import math
# import numpy as np
# import random
# import time

# 時間を計測
# start_time = time.time()
# LIMIT_TIME = 1.0

def move_cost(i: int, j: int, ni: int, nj: int) -> int:
    """ 移動コスト """
    return abs(i - ni) + abs(j - nj) + 1

# 位置を表す構造体
@dataclass
class Pos:
    i: int
    j: int

# 盤面の状態を表す構造体
@dataclass
class State:
    score: int          # 暫定スコア
    cost: int           # 操作コストの合計
    current_pos: Pos    # 現在の位置
    last5str: str       # 最近5手の文字列
    get_str: set        # 取得した文字列の集合
    last_idx: int      # Beam[i-1][どこ] から遷移したか（ただし初期状態では -1 としておく）

# ビームサーチを行う関数
def beam_search():
    # 2 次元配列 beam を用意し、0 手目の状態を設定
    MAX_MOVE = 5000
    beam = [list()]
    beam[0].append(State(0, 0, Pos(si, sj), "", set(), -1))

    # ビームサーチ
    for bi in range(MAX_MOVE):
        if bi <= 10:    # 10手までは幅を広げる
            WIDTH = 100
        else:
            # WIDTH = 2
            WIDTH = 10
        candidate = list()
        dbeam = dict()
        dbeam_strset = dict()
        for bj in range(len(beam[bi])):
            dbeam_strset[beam[bi][bj].last5str] = beam[bi][bj].get_str
            if beam[bi][bj].last5str not in dbeam:
                dbeam[beam[bi][bj].last5str] = [bj]
            else:
                dbeam[beam[bi][bj].last5str].append(bj)
        # for bj in range(len(beam[bi])):
        for last5str, bj_list in dbeam.items():
            for c, pos_list in dA.items():
                new5str = last5str[-4:] + c
                if len(new5str) == 5 and new5str in t:
                    new_get_str = dbeam_strset[last5str] | set([new5str])
                else:
                    new_get_str = dbeam_strset[last5str]
                not_get_strs = t - new_get_str
                score = 1000 * (len(new_get_str) + 1)
                for k in range(1, max(5, len(new5str)+1)):   # 1文字から4文字までの文字列が含まれていればscoreに加算
                    for not_get_str in not_get_strs:
                        if not_get_str[:k] == new5str[-k:]:
                            score += k ** 4

                for bj in bj_list:
                    for pos in pos_list:
                        cost = beam[bi][bj].cost + move_cost(beam[bi][bj].current_pos.i, beam[bi][bj].current_pos.j, pos.i, pos.j)
                        if len(new_get_str) == M:   # 全ての文字列を取得している場合
                            score = max(10000 - cost, 1001) * M
                        # 候補に追加
                        candidate.append(State(score, cost, pos, new5str, new_get_str, bj))
        # ソートして beam[i+1] の結果を計算する
        candidate.sort(key = lambda s: (-s.score, s.cost))
        beam.append(candidate[:WIDTH])  # 多くとも candidate の上位 WIDTH 件しか記録しない
        # print(f"bi:{bi}, score:{beam[-1][0].score}, cost:{beam[-1][0].cost}, get_str:{len(beam[-1][0].get_str)}, last5str:{beam[-1][0].last5str}", file=sys.stderr)
        if len(beam[-1][0].get_str) == M: break  # 全ての文字列を取得している場合
    
    score = beam[-1][0].score
    # ビームサーチの復元
    current_idx = 0
    answer = [ None ] * (len(beam) - 1)
    for i in range(len(beam) - 1, 0, -1):
        answer[i - 1] = beam[i][current_idx].current_pos
        current_idx = beam[i][current_idx].last_idx
    return answer, score//M


# 入力
N, M = map(int, input().split())    # N:15, M:200
si, sj = map(int, input().split())  # 開始位置
A = [list(input()) for _ in range(N)] # N*Nの英大文字
# print(A, file=sys.stderr)
dA = dict()
for i in range(N):
    for j in range(N):
        if A[i][j] not in dA:
            dA[A[i][j]] = [Pos(i, j)]
        else:
            dA[A[i][j]].append(Pos(i, j))
# print(dA, file=sys.stderr)
t = set([input() for _ in range(M)])     # M個の5文字の英大文字

# ビームサーチを行って答えを出す（書籍とは異なり、ビームサーチの復元は関数の中で行う）
answer, score = beam_search()
print(f"score:{score}", file=sys.stderr)

# 出力
for pos in answer:
    print(pos.i, pos.j)
