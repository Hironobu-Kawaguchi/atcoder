# https://atcoder.jp/contests/ahc018/submissions/39276902
from enum import Enum
import sys
import time
from collections import defaultdict
from copy import deepcopy

import numpy as np
from scipy.spatial.distance import cdist
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

input = sys.stdin.readline

INF = 10**18
DEBUG = 0

#UnionFind
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
        return {r: self.members(r) for r in self.roots()}
    def __str__(self):
        return ' '.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

class GaussianProcess:
    def __init__(self, trains, results):
        self.trains = trains
        self.results = results

        k11 = self.kernel(self.trains, self.trains)
        self.k11_inv = np.linalg.inv(k11)
    
    def fit(self, test):
        k12 = self.kernel2(self.trains, test)
        #k22 = self.kernel(test, test)

        # 期待値
        y_test = np.dot(k12.T, np.dot(self.k11_inv, self.results))
        # 分散
        #vars = k22 - np.dot(k12.T, np.dot(self.k11_inv, k12))
        # 標準偏差
        #y_test_std =  np.sqrt(np.diag(vars)).reshape(-1,1)

        return y_test

    s1 = 2
    s2 = 6000
    s3 = 0.1
    def kernel(self,x, x_p):
        return self.s1 * np.exp(-1.0 * cdist(x, x_p, 'sqeuclidean')/self.s2) + (self.s3 * np.eye(x.shape[0]))
    
    def kernel2(self,x, x_p):
        return self.s1 * np.exp(-1.0 * cdist(x, x_p, 'sqeuclidean')/self.s2)

class Pos:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x
    def __eq__(self, other):
        if self.y == other.y and self.x == other.x:
            return True
        else:
            return False
    def __hash__(self):
        return hash((self.y, self.x))


class Response(Enum):
    NOT_BROKEN = 0
    BROKEN = 1
    FINISH = 2
    INVALID = -1

class Graph:
    y_axis = defaultdict(list)
    x_axis = defaultdict(list)
    num_of_points = 0
    point_to_index = dict()
    index_to_point = []


    def __init__(self, N):
        self.N = N
    
    def add_point(self, y, x):
        if (y,x) in self.point_to_index:
            return
        if not (0 <= y < self.N):
            return
        if not (0 <= x < self.N):
            return
        self.point_to_index[(y,x)] = self.num_of_points
        self.index_to_point.append([y,x])
        self.y_axis[y].append(x)
        self.x_axis[x].append(y)
        self.num_of_points += 1

    def create_graph(self):
        self.costs = [None for i in range(self.num_of_points)]
        self.graph = [[] for i in range(self.num_of_points)]
        self.uf = UnionFind(self.num_of_points)

        self.fr = []
        self.to = []
        self.edges = []
        for k,v in self.y_axis.items():
            y = k
            xs = sorted(v)
            for i in range(len(xs) - 1):
                x0, x1 = xs[i], xs[i+1]
                dist = abs(x1-x0)
                p1 = self.point_to_index[(y,x0)]
                p2 = self.point_to_index[(y,x1)]
                self.fr.append(p1)
                self.to.append(p2)
                self.edges.append([p1, p2, dist])

                self.graph[self.point_to_index[(y,x0)]].append([self.point_to_index[(y,x1)], dist])
                self.graph[self.point_to_index[(y,x1)]].append([self.point_to_index[(y,x0)], dist])
        
        for k,v in self.x_axis.items():
            x = k
            ys = sorted(v)
            for i in range(len(ys) - 1):
                y0, y1 = ys[i], ys[i+1]
                dist = abs(y1-y0)
                p1 = self.point_to_index[(y0,x)]
                p2 = self.point_to_index[(y1,x)]
                self.fr.append(p1)
                self.to.append(p2)
                self.edges.append([p1, p2, dist])

                self.graph[self.point_to_index[(y0,x)]].append([self.point_to_index[(y1,x)], dist])
                self.graph[self.point_to_index[(y1,x)]].append([self.point_to_index[(y0,x)], dist])

        self.costs2 = [INF for i in range(len(self.edges))]
    
    def update_weight(self, y, x, cost):
        self.costs[self.point_to_index[(y,x)]] = cost

    def update_graph(self):
        for i in range(len(self.edges)):
            fr, to, dist = self.edges[i]
            self.costs2[i] = ( self.costs[fr] + self.costs[to] ) * (dist-1) + 1
        self.update_dist()

    dist_cache = dict()
    def clear_cache(self):
        self.dist_cache = dict()

    def update_dist(self):
        self.graph2 = csr_matrix((self.costs2, (self.fr, self.to)), (self.num_of_points, self.num_of_points))
        
    def dijkstra(self, y, x):
        s = self.point_to_index[(y,x)]
        if s in self.dist_cache:
            return self.dist_cache[s]
        dist = dijkstra(self.graph2, directed = False, indices = s)
        self.dist_cache[s] = deepcopy(dist)
        return dist
    
    def revert_route(self, fr :Pos, to: Pos):
        fr_y, fr_x = fr.y, fr.x
        to_y, to_x = to.y, to.x
        dist = self.dijkstra(fr_y, fr_x)
        now = self.point_to_index[(to_y, to_x)]
        goal = self.point_to_index[(fr_y, fr_x)]
        points = []
        points.append(Pos(to_y, to_x))
        while now != goal:
            cost_now = self.costs[now]
            for idx, d in self.graph[now]:
                cost_to = self.costs[idx]
                cost = ( cost_now + cost_to ) * (d-1) + 1
                if dist[idx] == dist[now] - cost:
                    now = idx
                    y,x = self.index_to_point[idx]
                    points.append(Pos(y, x))
                    break
        return points
    
    def get_dist(self, s: Pos, g: Pos):
        dist = self.dijkstra(s.y, s.x)
        return dist[self.point_to_index[(g.y, g.x)]]
    
    def connect(self, s: Pos, g: Pos):
        x = self.point_to_index[(s.y, s.x)]
        y = self.point_to_index[(g.y, g.x)]
        self.uf.union(x, y)
    
    def is_same(self, s: Pos, g: Pos):
        x = self.point_to_index[(s.y, s.x)]
        y = self.point_to_index[(g.y, g.x)]
        return self.uf.same(x, y)


class Field:

    def __init__(self, N: int, C: int, power_list):
        self.C = C
        self.is_broken = [[False] * N for _ in range(N)]
        self.used_power = [[0] * N for _ in range(N)]
        self.attack_count = [[0] * N for _ in range(N)]
        self.at_least = [[0] * N for _ in range(N)]
        self.at_most = [[0] * N for _ in range(N)]
        self.total_cost = 0
        self.power_list = power_list

    def query(self, y: int, x: int, power: int) -> Response:
        self.total_cost += power + self.C
        print(f"{y} {x} {power}", flush=True)
        res = Response(int(input()))
        self.used_power[y][x] += power
        self.at_most[y][x] += power
        self.attack_count[y][x] += 1
        if res in (Response.BROKEN, Response.FINISH):
            self.is_broken[y][x] = True
        else:
            self.at_least[y][x] += power
        return res
    
    def get_weight(self, y, x):
        if self.is_broken[y][x]:
            #return int(self.at_least[y][x] * 0.3 + self.at_most[y][x] * 0.7)
            return self.used_power[y][x]
        else:
            used = self.used_power[y][x]
            next_power = used + self.power_list[self.attack_count[y][x]]
            return (used + next_power) // 2


class Solver:

    # TODO: 後でもっとちゃんと考察する
    power_list_1   = [10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180,
                      200, 240, 260, 280, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 1000]
    power_list_2   = [10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180,
                     200, 240, 260, 280, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 1000]
    power_list_4   = [10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180,
                     200, 240, 260, 280, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 1000]
    power_list_8   = [10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180,
                     200, 240, 260, 280, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 1000]
    power_list_16  = [30, 60, 100, 150, 200, 300, 400, 500, 500, 500, 500, 500, 500, 500, 500, 500]
    power_list_32  = [60, 120, 180, 240, 300, 350, 400, 500, 500, 500, 500, 500, 500, 500, 500, 500]
    power_list_64  = [100, 200, 200, 300, 400, 400, 500, 500, 500, 500, 500, 500, 500, 500]
    power_list_128 = [200, 400, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]

    power_lists = {
        1: power_list_1,
        2: power_list_2,
        4: power_list_4,
        8: power_list_8,
        16: power_list_16,
        32: power_list_32,
        64: power_list_64,
        128: power_list_128,
    }    

    def __init__(self, N: int, source_pos, house_pos, C: int):
        self.start_time = time.time()
        self.N = N
        self.source_pos = np.array(source_pos)
        self.house_pos = np.array(house_pos)
        self.C = C
        self.power_list = self.power_lists[C]
        self.field = Field(N, C, self.power_list)
        self.graph = Graph(N)
        self.gaussian_process = None
    
    def bolling(self, y, x):
        if not (0 <= y < self.N):
            return
        if not (0 <= x < self.N):
            return
        for i in range(2): # TODO 時間が足りないので2回ずつまとめて掘る
            power = self.power_list[self.field.attack_count[y][x]]
            if self.field.is_broken[y][x]:
                return Response.BROKEN
            ret = self.field.query(y, x, power)
            if ret in (Response.BROKEN, Response.FINISH):
                return ret
        return ret
    
    def graph_update(self):
        """グラフの重み(とついでに標準偏差)を更新する"""

        self.graph.clear_cache()

        self.sigma = dict()
        grid = []
        for y, x in self.graph.index_to_point:
            if self.field.is_broken[y][x]: #すでに壊されていたら実際の値を使う
                continue
            else:
                grid.append([y,x])
        
        mu = self.gaussian_process.fit(np.array(grid))
        idx = 0
        for y,x in self.graph.index_to_point:
            if self.field.is_broken[y][x]: #すでに壊されていたら実際の値を使う
                m = self.field.get_weight(y, x)
                #m = (self.field.at_least[y][x] + self.field.at_most[y][x]) // 2
                s = 0
            elif self.field.used_power[y][x] != 0:
                m = self.field.get_weight(y, x)
                idx += 1
            #    m,s = mu[idx], sigma[idx][0]
            #    idx += 1
            #    m = self.field.used_power[y][x] * 2
            else:
                m = mu[idx]
                idx += 1
            m = int(m)
            m = min(m, 5000)
            m = max(m, 10)
            m = max(m, self.field.used_power[y][x])
            self.graph.update_weight(y, x, int(m))
            #self.sigma[(y, x)] = s
            if DEBUG:
                print("#estimate", y, x, m, s)

        self.graph.update_graph()

    def solve(self):

        grid_size = 10

        train_data = []
        train_data_set = set()
        results = []

        def add_tate_yoko(y, x):
            yy = y//grid_size * grid_size
            if yy != y:
                self.graph.add_point(yy, x)
            yy = -(-y//grid_size) * grid_size
            if yy != y:
                self.graph.add_point(yy, x)
            xx = x//grid_size * grid_size
            if xx != x:
                self.graph.add_point(y, xx)
            xx = -(-x//grid_size) * grid_size
            if xx != x:
                self.graph.add_point(y, xx)
        
        def add_train_data(y, x):
            train_data.append([y,x])
            train_data_set.add((y,x))
            results.append(self.field.get_weight(y, x))

        # とりあえず各水源と家を掘る
        for s in self.source_pos:
            y,x = s.y, s.x
            self.destruct(y, x)
            add_train_data(y, x)
            self.graph.add_point(y, x)
            add_tate_yoko(y,x)
        
        houses_index = []
        for s in self.house_pos:
            y,x = s.y, s.x
            self.destruct(y, x)
            self.graph.add_point(y, x)
            add_train_data(y, x)
            add_tate_yoko(y,x)
            houses_index.append(self.graph.point_to_index[(y,x)])
        houses_index = np.array(houses_index)

        # 10マスごとに地点を登録する
        for i in range(200):
            for j in range(200):
                y,x = i*grid_size, j*grid_size
                if x >= self.N:
                    x = self.N - 1
                if y >= self.N:
                    y = self.N - 1
                self.graph.add_point(y, x)
        
        self.graph.create_graph() #ここでグラフの形を固定する

        self.search_from_points = []
        for s in self.source_pos:
            self.search_from_points.append(s)
        
        connected = set()
        need_update = True
        while 1:
            if need_update:
                self.gaussian_process = GaussianProcess(np.array(train_data), np.array(results))
                need_update = False
            self.graph_update()

            min_dist = INF
            min_info = None
            for house in self.house_pos:
                if house in connected:
                    continue
                for from_pos in self.search_from_points:
                    if self.graph.is_same(from_pos, house):
                        continue
                    dist = self.graph.get_dist(house, from_pos)
                    if dist < min_dist:
                        min_dist = dist
                        min_info = [from_pos, house]
            from_pos, house = min_info
            route = self.graph.revert_route(from_pos, house)

            f = 1
            for pos in route:
                y, x = pos.y, pos.x
                if (y,x) not in train_data_set:
                    f = 0
                    need_update = True
                    return_code = self.bolling(y, x)
                    if return_code == Response.NOT_BROKEN:
                        break
                    add_train_data(y, x)
            
            if f or time.time() - self.start_time > 4.5:
                self.graph.connect(from_pos, house)
                connected.add(house)
                for i in range(len(route)-1):
                    self.move(route[i], route[i+1])
                for x in route:
                    self.search_from_points.append(x)

        # should receive Response.FINISH and exit before entering here
        raise AssertionError()

    def move(self, start: Pos, goal: Pos):
        # you can output comment
        print(f"# move from ({start.y},{start.x}) to ({goal.y},{goal.x})")

        # down/up
        if start.y < goal.y:
            for y in range(start.y, goal.y, 1):
                self.destruct(y, start.x)
        else:
            for y in range(start.y, goal.y, -1):
                self.destruct(y, start.x)

        # right/left
        if start.x < goal.x:
            for x in range(start.x, goal.x + 1, 1):
                self.destruct(goal.y, x)
        else:
            for x in range(start.x, goal.x - 1, -1):
                self.destruct(goal.y, x)

    def destruct(self, y: int, x: int):
        # excavate (y, x) with fixed power until destruction
        while not self.field.is_broken[y][x]:
            power = self.power_list[self.field.attack_count[y][x]]
            result = self.field.query(y, x, power)
            if result == Response.FINISH:
                print(f"total_cost={self.field.total_cost}", file=sys.stderr)
                sys.exit(0)
            elif result == Response.INVALID:
                print(f"invalid: y={y} x={x}", file=sys.stderr)
                sys.exit(1)


def main():
    N, W, K, C = [int(v) for v in input().split(" ")]
    source_pos = []
    house_pos = []
    for _ in range(W):
        y, x = (int(v) for v in input().split(" "))
        source_pos.append(Pos(y, x))
    for _ in range(K):
        y, x = (int(v) for v in input().split(" "))
        house_pos.append(Pos(y, x))

    solver = Solver(N, source_pos, house_pos, C)
    solver.solve()


if __name__ == "__main__":
    main()
