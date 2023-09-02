# Copyright [2022] <Copyright Eita Aoki (Thunder) >
import random
import numpy as np

# 座標を保持する
class Coord:
    def __init__(self, y = 0, x = 0):
        self.y_ = y
        self.x_ = x

H = 3  # 迷路の高さ
W = 4  # 迷路の幅
END_TURN = 4 # ゲーム終了ターン

# 一人ゲームの例
# 1ターンに上下左右四方向のいずれかに1マスずつ進む。
# 床にあるポイントを踏むと自身のスコアとなり、床のポイントが消える。
# END_TURNの時点のスコアを高くすることが目的
class MazeState:
    dx = [1, -1, 0, 0] # 右、左、下、上への移動方向のx成分
    dy = [0, 0, 1, -1] # 右、左、下、上への移動方向のy成分

    def __init__(self, seed=None):
        self.points_ = np.zeros((H,W), dtype=int) # 床のポイントを1~9で表現する
        self.turn_ = 0 # 現在のターン
        self.character_ = Coord()
        self.game_score_ = 0 # ゲーム上で実際に得たスコア
        if seed is not None:
            random.seed(seed)
            self.character_.y_ = random.randint(0, H-1)
            self.character_.x_ = random.randint(0, W-1)
            for y in range(H):
                for x in range(W):
                    if y == self.character_.y_ and x == self.character_.x_:
                        continue
                    self.points_[y,x] = random.randint(0, 9)

    def isDone(self):
        return self.turn_ == END_TURN

    def advance(self, action):
        self.character_.x_ += self.dx[action]
        self.character_.y_ += self.dy[action]
        point = self.points_[self.character_.y_, self.character_.x_]
        if point > 0:
            self.game_score_ += point
            self.points_[self.character_.y_, self.character_.x_] = 0
        self.turn_ += 1

    def legalActions(self):
        actions = []
        for action in range(4):
            ty = self.character_.y_ + self.dy[action]
            tx = self.character_.x_ + self.dx[action]
            if 0 <= ty < H and 0 <= tx < W:
                actions.append(action)
        return actions

    def __str__(self):
        ss = f"turn:\t{self.turn_}\n"
        ss += f"score:\t{self.game_score_}\n"
        for h in range(H):
            for w in range(W):
                if self.character_.y_ == h and self.character_.x_ == w:
                    ss += '@'
                elif self.points_[h,w] > 0:
                    ss += str(self.points_[h,w])
                else:
                    ss += '.'
            ss += '\n'
        return ss

State = MazeState

def randomAction(state):
    legal_actions = state.legalActions()
    return legal_actions[random.randint(0, len(legal_actions)-1)]

def playGame(seed):
    state = State(seed)
    print(state)
    while not state.isDone():
        state.advance(randomAction(state))
        print(state)

def main():
    playGame(121321)

if __name__ == "__main__":
    main()
