# https://atcoder.jp/contests/ahc026/tasks/ahc026_a

import sys
# import numpy as np

n, m = map(int, input().split())    # n: 200, m: 10
b = [list(map(int, input().split())) for _ in range(m)]

class WareHouse:
    def __init__(self, n, m, b):
        self.MAX_N = 200
        self.n = n
        self.m = m
        self.b = b
        self.pos = [-1] * (n+1)
        for i in range(self.m):
            for v in b[i]:
                self.pos[v] = i
        self.min_v = 1
        self.count = 0
        self.V = 0

    def move(self, v, to):
        frm = self.pos[v]
        j = self.b[frm].index(v)
        for jj in range(j, len(self.b[frm])):
            # print(frm, jj, *b[frm], file=sys.stderr)
            self.pos[self.b[frm][jj]] = to
            self.V += 1
        self.V += 1
        self.b[to] += self.b[frm][j:]
        self.b[frm] = self.b[frm][:j]
        print(f'{v} {to+1}')
        self.count += 1
        return

    def remove(self):
        v = self.min_v
        frm = self.pos[v]
        if self.b[frm][-1] != v: return False
        self.b[frm].pop()
        self.pos[v] = -1
        print(f'{v} 0')
        self.count += 1
        self.min_v += 1
        return True

    def select_move(self, frm):
        min_b = [self.MAX_N + 1] * m
        for i in range(m):
            for v in self.b[i]:
                min_b[i] = min(min_b[i], v)
        sorted_min_b = sorted([(min_b[i], -len(b[i]), i) for i in range(m)], reverse=True)
        if sorted_min_b[0][2] == frm:
            to = sorted_min_b[1][2]
            to_max_v = sorted_min_b[1][0]
        else:
            to = sorted_min_b[0][2]
            to_max_v = sorted_min_b[0][0]
        return to, to_max_v

    def solve(self):
        while True:
            while self.min_v <= self.MAX_N:
                if self.remove():
                    continue
                else:
                    break
            if self.min_v > self.MAX_N: break
            v = self.min_v
            frm = self.pos[v]

            # print(v, frm, *b[frm], file=sys.stderr)
            j = self.b[frm].index(v)
            min_upper = min(self.b[frm][j+1:])
            # print(v, frm, j, *b[frm], file=sys.stderr)

            min_upper = self.MAX_N + 1
            # min_upper_list = []
            # min_upper_idx = -1
            for jj in range(len(self.b[frm])-1, j, -1):
                if self.b[frm][jj] < min_upper:
                    min_upper = self.b[frm][jj]
                    # min_upper_idx = jj
                    to, to_max_v = self.select_move(frm)
                    if jj!=len(self.b[frm])-1 and min_upper < to_max_v:
                        # min_upper_list.append(jj)
                        v = self.b[frm][jj + 1]
                        self.move(v, to)
            # print(f'{v} {to+1}', file=sys.stderr)
            v = self.b[frm][j+1]
            to, to_max_v = self.select_move(frm)
            # sorted_len_b = sorted([(len(self.b[i]), i) for i in range(m)])
            # to = sorted_len_b[0][1] if sorted_len_b[0][1] != frm else sorted_len_b[1][1]
            self.move(v, to)
        return

wh = WareHouse(n, m, b)
wh.solve()
print("Count =", wh.count, file=sys.stderr)
print("Score =", max(1, 10000 - wh.V), file=sys.stderr)
# print(wh.b, file=sys.stderr)
