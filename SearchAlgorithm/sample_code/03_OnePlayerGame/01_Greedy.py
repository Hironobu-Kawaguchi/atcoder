# Copyright [2022] <Copyright Eita Aoki (Thunder) >

import random
from dataclasses import dataclass

# 座標を保持する
@dataclass
class Coord:
    y_: int = 0
    x_: int = 0

# ゲームの評価スコアの型を決めておく
ScoreType = int
INF = 1000000000  # あり得ないぐらい大きなスコアの例を用意しておく

H = 3  # 迷路の高さ
W = 4  # 迷路の幅
END_TURN = 4  # ゲーム終了ターン

dx = [1, -1, 0, 0]  # 右、左、下、上への移動方向のx成分
dy = [0, 0, 1, -1]  # 右、左、下、上への移動方向のy成分


class MazeState:
    def __init__(self, seed=None):
        self.points_ = [[0 for _ in range(W)] for _ in range(H)]  # 床のポイントを1~9で表現する
        self.turn_ = 0  # 現在のターン
        self.character_ = Coord()
        self.game_score_ = 0  # ゲーム上で実際に得たスコア
        self.evaluated_score_ = 0  # 探索上で評価したスコア

        if seed is not None:
            random.seed(seed)
            self.character_.y_ = random.randrange(H)
            self.character_.x_ = random.randrange(W)

            for y in range(H):
                for x in range(W):
                    if y == self.character_.y_ and x == self.character_.x_:
                        continue
                    self.points_[y][x] = random.randrange(10)

    # ゲームの終了判定
    def isDone(self):
        return self.turn_ == END_TURN

    # 探索用の盤面評価をする
    def evaluateScore(self):
        self.evaluated_score_ = self.game_score_  # 簡単のため、まずはゲームスコアをそのまま盤面の評価とする

    # 指定したactionでゲームを1ターン進める
    def advance(self, action):
        self.character_.x_ += dx[action]
        self.character_.y_ += dy[action]
        point = self.points_[self.character_.y_][self.character_.x_]
        if point > 0:
            self.game_score_ += point
            self.points_[self.character_.y_][self.character_.x_] = 0
        self.turn_ += 1

    # 現在の状況でプレイヤーが可能な行動を全て取得する
    def legalActions(self):
        actions = []
        for action in range(4):
            ty = self.character_.y_ + dy[action]
            tx = self.character_.x_ + dx[action]
            if 0 <= ty < H and 0 <= tx < W:
                actions.append(action)
        return actions

    # 現在のゲーム状況を文字列にする
    def __str__(self):
        res = []
        res.append(f"turn:\t{self.turn_}")
        res.append(f"score:\t{self.game_score_}")
        for h in range(H):
            row = []
            for w in range(W):
                if self.character_.y_ == h and self.character_.x_ == w:
                    row.append('@')
                elif self.points_[h][w] > 0:
                    row.append(str(self.points_[h][w]))
                else:
                    row.append('.')
            res.append(''.join(row))
        return '\n'.join(res)


def randomAction(state):
    legal_actions = state.legalActions()
    return random.choice(legal_actions)


def greedyAction(state):
    legal_actions = state.legalActions()
    best_score = -INF  # 絶対にありえない小さな値でベストスコアを初期化する
    best_action = -1  # ありえない行動で初期化する
    for action in legal_actions:
        now_state = MazeState()
        now_state.character_ = Coord(state.character_.y_, state.character_.x_)
        now_state.points_ = [row[:] for row in state.points_]
        now_state.game_score_ = state.game_score_
        now_state.turn_ = state.turn_
        now_state.advance(action)
        now_state.evaluateScore()
        if now_state.evaluated_score_ > best_score:
            best_score = now_state.evaluated_score_
            best_action = action
    return best_action


def playGame(seed):
    state = MazeState(seed)
    print(state)
    while not state.isDone():
        state.advance(greedyAction(state))
        print(state)


if __name__ == "__main__":
    playGame(121321)
