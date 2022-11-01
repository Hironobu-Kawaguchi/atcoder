# https://atcoder.jp/contests/intro-heuristics/tasks/intro_heuristics_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import bisect

D = int(input())
c = list(map(int, (input().split())))
s = [[int(i) for i in input().split()] for _ in range(D)]
t = [int(input()) for _ in range(D)]

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
        last = [-1] * self.typenumber
        for d in range(self.days):
            self.score += self.satisfaction[d][self.out[d]-1]
            self.ds[self.out[d]-1].append(d+1)
            self.ds[self.out[d]-1].sort()
            last[self.out[d]-1] = d
            for i in range(self.typenumber):
                self.score -= self.cost[i] * (d - last[i])
        return self.score

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
score = cs.new(t)
# print(score)

M = int(input())
for i in range(M):
    d, q = map(int, input().split())
    score = cs.change(d, q)
    print(score)



# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# import sys
# it = map(int, sys.stdin.buffer.read().split())
# N = next(it)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
