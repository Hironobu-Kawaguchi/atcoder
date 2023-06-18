# https://atcoder.jp/contests/ahc018/submissions/39276907
import copy
import random
import math
from enum import Enum
from typing import List
import sys
from time import perf_counter
from collections import defaultdict
from collections import deque
from heapq import heapify, heappop, heappush
import networkx as nx

########################################################################
OUT = 1     # 1:本番, 0:試験
########################################################################
N = 200
adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    def size(self, x):
        return -self.parents[self.find(x)]
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

class Pos:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x
        self.id = y * N + x

class Edge:
    def __init__(self, pa, pb, eid):
        if pa.id < pb.id:
            self.p1 = pa
            self.p2 = pb
        else:
            self.p1 = pb
            self.p2 = pa
        self.dist = abs(pa.x - pb.x) + abs(pa.y - pb.y)
        self.eid = eid

class Response(Enum):
    NOT_BROKEN = 0
    BROKEN = 1
    FINISH = 2
    INVALID = -1

class Field:
    def __init__(self, N: int, C: int, S, source_pos, house_pos, uf):
        self.C = C
        self.is_broken = [[False] * N for _ in range(N)]
        self.damage = [[0] * N for _ in range(N)]
        self.total_cost = 0
        self.S = S
        self.source_pos = source_pos
        self.house_pos = house_pos
        self.uf = uf

    def query(self, y: int, x: int, power: int) -> Response:
        self.total_cost += power + self.C
        print(f"{y} {x} {power}", flush=True)
        if OUT == 1:
            res = Response(int(input()))
            if res in (Response.BROKEN, Response.FINISH):
                self.is_broken[y][x] = True
        elif OUT == 0:
            if self.S[y][x] == 0:
                res = Response.INVALID
            elif self.S[y][x] - power > 0:
                self.S[y][x] -= power
                res = Response.NOT_BROKEN
            else:
                self.S[y][x] = 0
                self.is_broken[y][x] = True
                for dy, dx in adj:
                    if 0 <= y + dy < N and 0 <= x + dx < N:
                        if self.is_broken[y+dy][x+dx] == True:
                            self.uf.union(y*N + x, (y+dy)*N + x+dx)
                if self.judge_finish() == True:
                    res = Response.FINISH
                else:
                    res = Response.BROKEN
        return res

    def judge_finish(self):
        pos0 = self.source_pos[0]
        for pos in self.house_pos:
            if not self.uf.same(pos0.id, pos.id):
                return False
        return True

class Solver:
    def __init__(self, N: int, source_pos: List[Pos], house_pos: List[Pos], C: int, S, uf):
        self.N = N
        self.source_pos = source_pos
        self.house_pos = house_pos
        self.C = C
        self.field = Field(N, C, S, source_pos, house_pos, uf)

    def solveOld(self): # NetworkXで
        # 最小全域木
        all_pos = []
        all_pos.extend(self.source_pos)
        all_pos.extend(self.house_pos)
        Nlocs = len(all_pos)
        Nslocs = len(self.source_pos)
        Nhlocs = len(self.house_pos)
        E = []
        Edges = []
        eid = 0
        for i in range(Nlocs):
            for j in range(i+1, Nlocs):
                e = Edge(all_pos[i], all_pos[j], eid)
                eid += 1
                Edges.append(e)
                E.append((e.dist, i, j, e.eid))
        E.sort(key = lambda x: (x[0]))

        uf2 = UnionFind(Nlocs)
        # 水源同士は連結とみなす
        for i in range(Nslocs):
            uf2.union(0, i)

        Gx = nx.empty_graph() # 探索グラフ
        for p in self.source_pos:
            Gx.add_node(p.id)
        for p in self.house_pos:
            Gx.add_node(p.id)

        cnt_connected = 0 # 連結した累積数

        # 必要だけ繰り返し
        while cnt_connected < len(self.house_pos):
            # print("loop", iloop, file=sys.stderr)
            # コストの小さい方から連結でないijペアを２つ選択
            pairs = []
            minc = 10**18
            for ie, ee in enumerate(E):
                i, j = ee[1], ee[2] # i, j : all_posのid
                if uf2.same(i, j):
                    continue
                else:
                    # eid = E[i][3]
                    PosS = all_pos[i]
                    PosG = all_pos[j]
                    if not Gx.has_edge(PosS.id, PosG.id):
                        self.moveG(Gx, PosS, PosG) # 辺を張る（まだ繋いでない）

                    pairs.append((i, j))
                    c, path = nx.single_source_dijkstra(Gx, PosS.id, PosG.id, cutoff=10**18, weight='weight')
                    # print("dijk", c, file=sys.stderr)
                    # avec = c / (abs(PosS.x - PosG.x) + abs(PosS.y - PosG.y))
                    # if avec < 400: # 良いので即採用
                    if c < 20000: # 良いので即採用
                        self.connectPosGraph(Gx, path, all_pos[i], all_pos[j])
                        uf2.union(i, j)
                        cnt_connected += 1
                        break

                    if c < minc:
                        ii, jj = i, j
                        minc = c
                        minpath = path

                    if len(pairs) == min(2, Nlocs-1):
                        # pairsの中の最小に対して連結
                        self.connectPosGraph(Gx, minpath, all_pos[ii], all_pos[jj])
                        uf2.union(ii, jj)
                        cnt_connected += 1
                        break

        # should receive Response.FINISH and exit before entering here
        raise AssertionError()

    def connectPosGraph(self, Gx, path, start: Pos, goal: Pos):
        # 与えられた経路で連結する
        for i in range(len(path) - 1):
            p0ID, p1ID = path[i], path[i+1]
            p0 = Pos(p0ID // N, p0ID % N)
            p1 = Pos(p1ID // N, p1ID % N)

            # 完全掘削
            self.moveLine(p0, p1) 
            # self.moveLineDiag(p0, p1) 
            if self.field.uf.same(start.id, goal.id):
                # Gxの重み更新（接続した辺は重みゼロとする）        
                Gx[p0ID][p1ID]['weight'] = abs(p0.y - p1.y) + abs(p0.x - p1.x)
        return

    def moveG(self, Gx, start: Pos, goal: Pos, choice=0):
        # you can output comment
        print(f"# move from ({start.y},{start.x}) to ({goal.y},{goal.x})")
        num = self.destruct(start.y, start.x, POW2, 10000)
        num = self.destruct(goal.y, goal.x, POW2, 10000)

        SOFT = 3000
        # ２点間の距離から分割数 ndiv の決定
        ddd = abs(start.x - goal.x) + abs(start.y - goal.y)
        if ddd <= DDIV:
            # ok = self.moveLine(start, goal)
            # つなぐ代わりにGxに頂点と辺を追加
            ok = True
            num0 = self.destruct(start.y, start.x, POW2, 10000)
            num0 = self.destruct(goal.y, goal.x, POW2, 10000)
            ws = self.field.damage[start.y][start.x]
            wg = self.field.damage[goal.y][goal.x]
            Gx.add_edge(start.id, goal.id, weight=(ws+wg)//2*ddd)
            # print("connected", start.id, goal.id, file=sys.stderr)
            return ok
        elif ddd <= DDIV * 2:
            kouho = []
            flag = False
            x0 = (start.x + goal.x) // 2
            y0 = (start.y + goal.y) // 2
            p0 = Pos(y0, x0)
            p2a = Pos(y0, x0) # ダミー
            p2b = Pos(y0, x0) # ダミー
            num0 = self.destruct(p0.y, p0.x, POW2, NUMMAX)
            # kouho.append((p0, num0))
            kouho.append((p0, self.field.damage[p0.y][p0.x]))
            # if num0 <= 1:
            if self.field.damage[p0.y][p0.x] <= SOFT and self.field.is_broken[p0.y][p0.x] == True:
                cen = p0
                flag = True
            if flag == False:
                dx0 = x0 - start.x
                dy0 = y0 - start.y
                x2a = x0 - dy0*2//3
                y2a = y0 + dx0*2//3
                x2b = x0 + dy0*2//3
                y2b = y0 - dx0*2//3
                if 0 <= x2a < N and 0 <= y2a < N and choice != 2:
                    p2a = Pos(y2a, x2a)
                    num2a = self.destruct(p2a.y, p2a.x, POW2, NUMMAX)
                    # kouho.append((p2a, num2a))
                    kouho.append((p2a, self.field.damage[p2a.y][p2a.x]))
                    # if num2a == 1:
                    if self.field.damage[p2a.y][p2a.x] <= SOFT and self.field.is_broken[p2a.y][p2a.x] == True:
                        cen = p2a
                        flag = True
                        choice = 1
                if 0 <= x2b < N and 0 <= y2b < N and choice != 1:
                    p2b = Pos(y2b, x2b)
                    num2b = self.destruct(p2b.y, p2b.x, POW2, NUMMAX)
                    # kouho.append((p2b, num2b))
                    kouho.append((p2b, self.field.damage[p2b.y][p2b.x]))
                    # if num2b == 1:
                    if self.field.damage[p2b.y][p2b.x] <= SOFT and self.field.is_broken[p2b.y][p2b.x] == True:
                        cen = p2b
                        flag = True
                        choice = 2
            if flag == False: # まだ決まっていない場合
                kouho.sort(key = lambda x: (x[1]))
                cen = kouho[0][0]
                if cen == p2a:
                    choice = 1
                elif cen == p2b:
                    choice = 2
                else:
                    choice = 0
            ok1 = self.moveG(Gx, start, cen, choice)
            ok2 = self.moveG(Gx, cen, goal, choice)
            if ok1 == True and ok2 == True:
                return True
            else:
                return False
        else:
            kouho = []
            flag = False
            x0 = (start.x + goal.x) // 2
            y0 = (start.y + goal.y) // 2
            p0 = Pos(y0, x0)
            p1a = Pos(y0, x0) # ダミー
            p1b = Pos(y0, x0) # ダミー
            p2a = Pos(y0, x0) # ダミー
            p2b = Pos(y0, x0) # ダミー
            num0 = self.destruct(p0.y, p0.x, POW2, NUMMAX)
            # kouho.append((p0, num0))
            kouho.append((p0, self.field.damage[p0.y][p0.x]))
            if num0 <= 1:
                cen = p0
                flag = True
            if flag == False:
                dx0 = x0 - start.x
                dy0 = y0 - start.y
                x1a = x0 - dy0//3
                y1a = y0 + dx0//3
                x1b = x0 + dy0//3
                y1b = y0 - dx0//3
                if 0 <= x1a < N and 0 <= y1a < N and choice != 2:
                    p1a = Pos(y1a, x1a)
                    num1a = self.destruct(p1a.y, p1a.x, POW2, NUMMAX)
                    # kouho.append((p1a, num1a))
                    kouho.append((p1a, self.field.damage[p1a.y][p1a.x]))
                    # if num1a == 1:
                    if self.field.damage[p1a.y][p1a.x] <= SOFT and self.field.is_broken[p1a.y][p1a.x] == True:
                        cen = p1a
                        flag = True
                if 0 <= x1b < N and 0 <= y1b < N and choice != 1:
                    p1b = Pos(y1b, x1b)
                    num1b = self.destruct(p1b.y, p1b.x, POW2, NUMMAX)
                    # kouho.append((p1b, num1b))
                    kouho.append((p1b, self.field.damage[p1b.y][p1b.x]))
                    # if num1b == 1:
                    if self.field.damage[p1b.y][p1b.x] <= SOFT and self.field.is_broken[p1b.y][p1b.x] == True:
                        cen = p1b
                        flag = True
            if flag == False:
                dx0 = x0 - start.x
                dy0 = y0 - start.y
                x2a = x0 - dy0*2//3
                y2a = y0 + dx0*2//3
                x2b = x0 + dy0*2//3
                y2b = y0 - dx0*2//3
                if 0 <= x2a < N and 0 <= y2a < N and choice != 2:
                    p2a = Pos(y2a, x2a)
                    num2a = self.destruct(p2a.y, p2a.x, POW2, NUMMAX)
                    # kouho.append((p2a, num2a))
                    kouho.append((p2a, self.field.damage[p2a.y][p2a.x]))
                    # if num2a == 1:
                    if self.field.damage[p2a.y][p2a.x] <= SOFT and self.field.is_broken[p2a.y][p2a.x] == True:
                        cen = p2a
                        flag = True
                        choice = 1
                if 0 <= x2b < N and 0 <= y2b < N and choice != 1:
                    p2b = Pos(y2b, x2b)
                    num2b = self.destruct(p2b.y, p2b.x, POW2, NUMMAX)
                    # kouho.append((p2b, num2b))
                    kouho.append((p2b, self.field.damage[p2b.y][p2b.x]))
                    # if num2b == 1:
                    if self.field.damage[p2b.y][p2b.x] <= SOFT and self.field.is_broken[p2b.y][p2b.x] == True:
                        cen = p2b
                        flag = True
                        choice = 2
            if flag == False: # まだ決まっていない場合
                kouho.sort(key = lambda x: (x[1]))
                cen = kouho[0][0]
                if cen == p2a:
                    choice = 1
                elif cen == p2b:
                    choice = 2
                else:
                    choice = 0
            ok1 = self.moveG(Gx, start, cen, choice)
            ok2 = self.moveG(Gx, cen, goal, choice)
            if ok1 == True and ok2 == True:
                return True
            else:
                return False

    def modpow(self, pow, cnt):
        # 前回の硬さに応じてパワーを修正
        if cnt == 1:
            pow = max(int(pow * POWERDOWN), 10)
        elif cnt >= 2:
            pow = min(int(pow * POWERUP), 350)
        return pow

    def moveLine(self, start: Pos, goal: Pos):
        # 完全に壊して完全に２点間をつなぐ
        # you can output comment
        print(f"# moveLine from ({start.y},{start.x}) to ({goal.y},{goal.x})")

        pow = POW1
        type = 0
        # 角2箇所の掘削回数を比較して小さい方を採用
        num1 = self.destruct(start.y, goal.x, POW2, NUMMAX)
        num2 = self.destruct(goal.y, start.x, POW2, NUMMAX)
        if self.field.damage[start.y][goal.x] < self.field.damage[goal.y][start.x]:
            type = 1
        else:
            type = 2

        if start.x < goal.x:
            dx = 1
        else:
            dx = -1
        if start.y < goal.y:
            dy = 1
        else:
            dy = -1

        if type == 1:
            # right/left
            for x in range(start.x, goal.x + dx, dx):
                cnt = self.destruct(start.y, x, pow, 10000)
                pow = self.modpow(pow, cnt)
                if self.field.uf.same(start.id, goal.id):
                    return True
            # down/up
            for y in range(start.y, goal.y + dy, dy):
                cnt = self.destruct(y, goal.x, pow, 10000)
                pow = self.modpow(pow, cnt)
                if self.field.uf.same(start.id, goal.id):
                    return True
        else:
            # down/up
            for y in range(start.y, goal.y + dy, dy):
                cnt = self.destruct(y, start.x, pow, 10000)
                pow = self.modpow(pow, cnt)
                if self.field.uf.same(start.id, goal.id):
                    return True
            # right/left
            for x in range(start.x, goal.x + dx, dx):
                cnt = self.destruct(goal.y, x, pow, 10000)
                pow = self.modpow(pow, cnt)
                if self.field.uf.same(start.id, goal.id):
                    return True

        return True

    def moveLineDiag(self, start: Pos, goal: Pos):
        # 完全に壊して完全に２点間をつなぐ（斜めに）
        pow = POW1
        nx = goal.x - start.x
        ny = goal.y - start.y
        if nx < 0:
            dirx = -1
        else:
            dirx = 1
        if ny < 0:
            diry = -1
        else:
            diry = 1
        nmove = abs(nx) + abs(ny)
        movex = []
        for j in range(abs(nx)):
            movex.append(int(nmove*(j+1)/abs(nx))-1)
        xnow = start.x
        ynow = start.y
        for i in range(nmove):
            if i in movex:
                xnow += dirx
            else:
                ynow += diry
            cnt = self.destruct(ynow, xnow, pow, 10000)
            pow = self.modpow(pow, cnt)
        return True

    def destruct(self, y: int, x: int, power, mx):
        # excavate (y, x) with fixed power until destruction
        cnt = 0
        while not self.field.is_broken[y][x] and cnt < mx:
            result = self.field.query(y, x, power)
            cnt += 1
            self.field.damage[y][x] += power
            if result == Response.FINISH:
                print(f"{self.field.total_cost}", file=sys.stderr)
                sys.exit(0)
            elif result == Response.INVALID:
                print(f"invalid: y={y} x={x}", file=sys.stderr)
                sys.exit(1)
        return cnt

def main():
    global POW1a, POW1b, POW1, POW2, POWERDOWN, POWERUP, NUMMAX, DDIV
    T_limit = 5.0
    t_begin = perf_counter()
    
    N, W, K, C = [int(v) for v in input().split(" ")]

    DDIV = 34 # 辺分割単位

    Cpow = math.log2(C) # 0(1) to 7(128)
    POW1a = 10 # 掘削パワー（壊すとき
    POW1 = int(POW1a + 15 * Cpow) # 0 to 7

    POWERDOWN = 0.9 - (7-Cpow) * 0.03
    POWERUP = 1.3 - (7-Cpow) * 0.03

    if C <= 2:
        NUMMAX = 10
        POW2 = 40
    elif C <= 4:
        NUMMAX = 7
        POW2 = 60
    elif C <= 6:
        NUMMAX = 5
        POW2 = 80
    else:
        NUMMAX = 4
        POW2 = 100

    #########
    TYPE = 0
    #########

    if OUT == 0:
        S = [list(map(int, input().split())) for i in range(N)]
    else:
        S = [[0]*N for _ in range(N)]

    source_pos = []
    house_pos = []
    for _ in range(W):
        y, x = (int(v) for v in input().split(" "))
        source_pos.append(Pos(y, x))
    for _ in range(K):
        y, x = (int(v) for v in input().split(" "))
        house_pos.append(Pos(y, x))

    uf = UnionFind(N**2)
    pos0 = source_pos[0]    
    for pos in source_pos:
        uf.union(pos0.id, pos.id)

    solver = Solver(N, source_pos, house_pos, C, S, uf)
    if TYPE == 0:
        solver.solveOld()


if __name__ == "__main__":
    main()

# 18
# score: 