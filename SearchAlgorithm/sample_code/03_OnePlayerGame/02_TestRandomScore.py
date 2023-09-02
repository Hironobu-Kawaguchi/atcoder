# Copyright [2022] <Copyright Eita Aoki (Thunder) >

import random

class Coord:
    def __init__(self, y=0, x=0):
        self.y_ = y
        self.x_ = x

INF = 1000000000
H = 3
W = 4
END_TURN = 4
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

class MazeState:
    def __init__(self, seed=None):
        self.points_ = [[0] * W for _ in range(H)]
        self.turn_ = 0
        self.character_ = Coord()
        self.game_score_ = 0
        self.evaluated_score_ = 0
        
        if seed is not None:
            random.seed(seed)
            self.character_.y_ = random.randint(0, H-1)
            self.character_.x_ = random.randint(0, W-1)
            for y in range(H):
                for x in range(W):
                    if y == self.character_.y_ and x == self.character_.x_:
                        continue
                    self.points_[y][x] = random.randint(1, 9)

    def isDone(self):
        return self.turn_ == END_TURN

    def evaluateScore(self):
        self.evaluated_score_ = self.game_score_

    def advance(self, action):
        self.character_.x_ += dx[action]
        self.character_.y_ += dy[action]
        point = self.points_[self.character_.y_][self.character_.x_]
        if point > 0:
            self.game_score_ += point
            self.points_[self.character_.y_][self.character_.x_] = 0
        self.turn_ += 1

    def legalActions(self):
        actions = []
        for action in range(4):
            ty = self.character_.y_ + dy[action]
            tx = self.character_.x_ + dx[action]
            if 0 <= ty < H and 0 <= tx < W:
                actions.append(action)
        return actions

    def __str__(self):
        result = f"turn:\t{self.turn_}\nscore:\t{self.game_score_}\n"
        for y in range(H):
            for x in range(W):
                if self.character_.y_ == y and self.character_.x_ == x:
                    result += '@'
                elif self.points_[y][x] > 0:
                    result += str(self.points_[y][x])
                else:
                    result += '.'
            result += '\n'
        return result

def randomAction(state):
    legal_actions = state.legalActions()
    return random.choice(legal_actions)

def greedyAction(state):
    legal_actions = state.legalActions()
    best_score = -INF
    best_action = -1
    for action in legal_actions:
        now_state = MazeState()
        now_state.__dict__ = state.__dict__.copy()  # Deep copy of current state
        now_state.advance(action)
        now_state.evaluateScore()
        if now_state.evaluated_score_ > best_score:
            best_score = now_state.evaluated_score_
            best_action = action
    return best_action

def testAiScore(game_number):
    score_mean = 0
    for _ in range(game_number):
        state = MazeState(0)
        while not state.isDone():
            state.advance(randomAction(state))
        score = state.game_score_
        score_mean += score
    score_mean /= game_number
    print(f"Score:\t{score_mean:.2f}")

if __name__ == "__main__":
    testAiScore(100)
