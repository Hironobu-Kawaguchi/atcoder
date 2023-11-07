# https://atcoder.jp/contests/ahc026/tasks/ahc026_a

import sys
# import numpy as np

n, m = map(int, input().split())    # n: 200, m: 10
b = [list(map(int, input().split())) for _ in range(m)]

class WareHouse:
    def __init__(self, n, b):
        self.n = n
        self.b = b
        self.pos = [-1] * (n+1)
        for i in range(m):
            for v in b[i]:
                self.pos[v] = i
        self.min_v = 1
        self.count = 0

    def move(self, v, to):
        frm = self.pos[v]
        j = self.b[frm].index(v)
        for jj in range(j, len(self.b[frm])):
            # print(frm, jj, *b[frm], file=sys.stderr)
            self.pos[self.b[frm][jj]] = to
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

    def solve(self):
        while True:
            while self.min_v < self.n+1:
                if self.remove():
                    continue
                else:
                    break
            if self.min_v == self.n+1: break
            v = self.min_v
            frm = self.pos[v]
            # print(v, frm, *b[frm], file=sys.stderr)
            j = self.b[frm].index(v) + 1    # 1つ上の位置
            # print(v, frm, j, *b[frm], file=sys.stderr)
            sorted_len_b = sorted([(len(self.b[i]), i) for i in range(m)])
            to = sorted_len_b[0][1] if sorted_len_b[0][1] != frm else sorted_len_b[1][1]
            # print(f'{v} {to+1}', file=sys.stderr)
            v = self.b[frm][j]
            self.move(v, to)
        return

wh = WareHouse(n, b)
wh.solve()
print(wh.count, file=sys.stderr)
# print(wh.b, file=sys.stderr)
