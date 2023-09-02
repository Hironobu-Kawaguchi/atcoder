# https://atcoder.jp/contests/intro-heuristics/tasks/intro_heuristics_a

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import time
import random
import copy
import math
import bisect

time_limmit = time.time() + 1.8
D = int(input())
c = list(map(int, (input().split())))
s = [[int(i) for i in input().split()] for _ in range(D)]

class ComputeScore():
    def __init__(self, days, cost, satisfaction):
        self.typenumber = 26
        self.days = days
        self.cost = cost
        self.satisfaction = satisfaction
        self.score = 0
        self.out = [0] * self.days
        self.ds =  [[0, self.days+1] for _ in range(self.typenumber)]

    def compute_cost(self, a, b):
        d = b - a
        return d * (d - 1) // 2

    def new(self, out):
        self.out = out
        self.score = 0
        last = [-1] * self.typenumber
        for d in range(self.days):
            self.score += self.satisfaction[d][self.out[d]-1]
            self.ds[self.out[d]-1].append(d+1)
            self.ds[self.out[d]-1].sort()
            last[self.out[d]-1] = d
            for i in range(self.typenumber):
                self.score -= self.cost[i] * (d - last[i])
        return self.score

    def get_new(self):
        self.score = 0
        last = [-1] * self.typenumber
        for d in range(self.days):
            loss = [0] * self.typenumber
            for i in range(self.typenumber):
                loss[i] += self.cost[i] * (d - last[i]) * (d - last[i] - 1) // 2
                loss[i] += self.satisfaction[d][i]
            best_loss = -1001001001001
            best_idx = -1
            for i in range(self.typenumber):
                if loss[i]>best_loss:
                    best_loss = loss[i]
                    best_idx = i
            self.out[d] = best_idx + 1

            self.score += self.satisfaction[d][self.out[d]-1]
            self.ds[self.out[d]-1].append(d+1)
            self.ds[self.out[d]-1].sort()
            last[self.out[d]-1] = d
            for i in range(self.typenumber):
                self.score -= self.cost[i] * (d - last[i])
        return self.score, self.out

    def change(self, day, new_q):
        old_q = self.out[day-1]
        # print(self.ds[old_q-1])
        idx = bisect.bisect_left(self.ds[old_q-1], day)
        prev = self.ds[old_q-1][idx-1]
        next = self.ds[old_q-1][idx+1]
        self.ds[old_q-1].pop(idx)
        # print(self.ds[old_q-1])
        self.score += (self.compute_cost(prev, day) + self.compute_cost(day, next) - self.compute_cost(prev, next)) * self.cost[old_q-1]
        # print(self.ds[new_q-1])
        idx = bisect.bisect_left(self.ds[new_q-1], day)
        prev = self.ds[new_q-1][idx-1]
        next = self.ds[new_q-1][idx]
        self.ds[new_q-1].insert(idx, day)
        # print(self.ds[new_q-1])
        self.out[day-1] = new_q
        self.score -= (self.compute_cost(prev, day) + self.compute_cost(day, next) - self.compute_cost(prev, next)) * self.cost[new_q-1]
        self.score += self.satisfaction[day-1][new_q-1] - self.satisfaction[day-1][old_q-1]
        return self.score

cs = ComputeScore(D, c, s)

# t = [int(input()) for _ in range(D)]
# t = [random.randrange(1,27) for _ in range(D)]
# score = cs.new(t)
score, t = cs.get_new()
# print(score, t)
# print(cs.new(t))
# print(score==cs.new(t))
# print(t)

# M = int(input())
# for i in range(M):
#     d, q = map(int, input().split())
#     score = cs.change(d, q)
#     print(score)

while time.time() < time_limmit:
    d = random.randrange(1, D+1)
    q = random.randrange(1, 27)
    new_cs = copy.copy(cs)
    new_score = cs.change(d, q)
    if new_score > score:
        # print(score, new_score, cs.out)
        score = new_score
        cs = copy.copy(cs)

for x in cs.out:
    print(x)
