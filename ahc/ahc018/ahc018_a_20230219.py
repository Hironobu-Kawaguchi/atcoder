from enum import Enum
from typing import List
import sys
import math
from collections import deque
import heapq

vx = [0, 1, 0, -1]
vy = [1, 0, -1, 0]

class Pos:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x


class Response(Enum):
    NOT_BROKEN = 0
    BROKEN = 1
    FINISH = 2
    INVALID = -1


class Field:

    def __init__(self, N: int, C: int):
        self.N = N
        self.C = C
        self.is_broken = [[False] * N for _ in range(N)]
        self.total_cost = 0
        self.max_sturdiness = [[5000] * N for _ in range(N)]
        self.min_sturdiness = [[10] * N for _ in range(N)]
        self.excavation = [[0] * N for _ in range(N)]
        self.is_source = [[False] * N for _ in range(N)]   # 水源
        self.dist_source = [[1001001] * N for _ in range(N)]   # 水源からの距離xC

    def update_is_source(self, y: int, x: int):
        self.is_source[y][x] = True

    def init_dist_source(self):
        print(f"# init_dist_source start")
        done = [[False] * self.N for _ in range(self.N)]
        h = []
        for y in range(self.N):
            for x in range(self.N):
                if self.is_source[y][x]:
                    heapq.heappush(h, (0, y, x))
                    # done[y][x] = True
        while h:
            dist, y, x = heapq.heappop(h)
            if done[y][x]: continue
            done[y][x] = True
            # 距離0なら水源になる
            if dist==0: self.is_source[y][x] = True
            self.dist_source[y][x] = dist
            # print(f"# dist_source {dist}, {y}, {x}")
            for i in range(4):
                ny = y + vy[i]
                nx = x + vx[i]
                if ny<0 or ny>=self.N or nx<0 or nx>=self.N: continue
                if done[ny][nx]: continue
                # 既に壊れていれば距離は増えない
                if self.is_broken[ny][nx]:
                    heapq.heappush(h, (dist, ny, nx))
                else:
                    heapq.heappush(h, (dist + 1, ny, nx))
                    # heapq.heappush(h, (dist + self.C, ny, nx))
                    # heapq.heappush(h, (dist + int(math.log2(self.C) + 2.1), ny, nx))
                    # heapq.heappush(h, (dist + int(math.log2(self.C) + 3.1), ny, nx))
        print(f"# init_dist_source finish")

    def predict_sturdiness(self, y: int, x: int):
        done = [[False] * self.N for _ in range(self.N)]
        q = deque([(y, x, self.max_sturdiness[y][x], self.min_sturdiness[y][x])])
        while q:
            oy, ox, mx, mn = q.popleft()
            done[oy][ox] = True
            if mx>=5000 and mn<=10: continue
            self.max_sturdiness[oy][ox] = min(self.max_sturdiness[oy][ox], mx)
            self.min_sturdiness[oy][ox] = max(self.min_sturdiness[oy][ox], mn)
            for i in range(4):
                ny = oy + vy[i]
                nx = ox + vx[i]
                if ny<0 or ny>=self.N or nx<0 or nx>=self.N: continue
                if done[ny][nx]: continue
                q.append((ny, nx, min(mx*4, 5000), max(mn//4, 10)))
                # q.append((ny, nx, min(mx*3, 5000), max(mn//3, 10)))
                # q.append((ny, nx, min(mx*2, 5000), max(mn//2, 10)))

    def calc_expected_sturdiness(self, y: int, x: int):
        # maxとminからコストの期待値を計算
        # mx = math.log2(self.max_sturdiness[y][x] - 10 + 1)
        # mn = math.log2(self.min_sturdiness[y][x] - 10 + 1)
        # av = pow(2, ((mx + mn) / 2))
        mx = (self.max_sturdiness[y][x] - 10) ** (1/5)
        mn = (self.min_sturdiness[y][x] - 10) ** (1/5)
        av = ((mx + mn) / 2) ** 5
        res = min(int(av) + 10, 5000)
        # print(f"expected_={res}, {y}, {x}, {self.max_sturdiness[y][x]}, {self.min_sturdiness[y][x]}", file=sys.stderr)
        return res

    def query(self, y: int, x: int, power: int) -> Response:
        self.total_cost += power + self.C
        self.excavation[y][x] += power
        print(f"{y} {x} {power}", flush=True)
        res = Response(int(input()))
        if res in (Response.BROKEN, Response.FINISH):
            self.is_broken[y][x] = True
            print(f"# max_sturdiness ({y},{x}) {self.max_sturdiness[y][x]} -> {self.excavation[y][x]}")
            self.max_sturdiness[y][x] = self.excavation[y][x]
        else:
            print(f"# min_sturdiness ({y},{x}) {self.min_sturdiness[y][x]} -> {self.excavation[y][x]+1}")
            self.min_sturdiness[y][x] = self.excavation[y][x] + 1
        return res


class Solver:

    def __init__(self, N: int, source_pos: List[Pos], house_pos: List[Pos], C: int):
        self.N = N
        self.source_pos = source_pos
        self.house_pos = house_pos
        self.C = C
        self.field = Field(N, C)
        for source in self.source_pos:
            self.field.update_is_source(source.y, source.x)
        self.field.init_dist_source()

    def solve(self):
        # break each source and house
        for source in self.source_pos:
            self.destruct(source.y, source.x)
        for house in self.house_pos:
            self.destruct(house.y, house.x)
        # calc expected cost from each source and house
        for source in self.source_pos:
            self.field.predict_sturdiness(source.y, source.x)
        for house in self.house_pos:
            self.field.predict_sturdiness(house.y, house.x)

        # from each house, go straight to the first source
        # for house in self.house_pos:
        #     self.move(house, self.source_pos[0])

        ### a-star
        while True:
            print(f"# move a-star start")
            ret = self.move_astar()
            print(f"# move a-star finish")
            if ret: break

        # should receive Response.FINISH and exit before entering here
        raise AssertionError()

    ### 重要な重みづけ
    def cost_function(self, y: int, x: int) -> int:
        # return 40 * self.field.dist_source[y][x] + self.field.calc_expected_sturdiness(y, x)
        # return 50 * self.field.dist_source[y][x] + self.field.calc_expected_sturdiness(y, x)
        # return 70 * self.field.dist_source[y][x] + self.field.calc_expected_sturdiness(y, x)
        # return 80 * self.field.dist_source[y][x] + self.field.calc_expected_sturdiness(y, x)
        # return 100 * self.field.dist_source[y][x] + self.field.calc_expected_sturdiness(y, x)
        # return 150 * self.field.dist_source[y][x] + self.field.calc_expected_sturdiness(y, x)
        return 200 * self.field.dist_source[y][x] + self.field.calc_expected_sturdiness(y, x)
        # return 300 * self.field.dist_source[y][x] + self.field.calc_expected_sturdiness(y, x)
        # return 500 * self.field.dist_source[y][x] + self.field.calc_expected_sturdiness(y, x)

    def move_astar(self) -> bool:
        done = [[False] * self.N for _ in range(self.N)]
        h = []
        for house in self.house_pos:
            if not self.field.is_source[house.y][house.x]:   # 既に水源と繋がっていれば不要
                cost = self.cost_function(house.y, house.x)
                heapq.heappush(h, (cost, house.y, house.x))
        while h:
            cost, y, x = heapq.heappop(h)
            if done[y][x]: continue
            done[y][x] = True
            if not self.field.is_broken[y][x]:
                self.destruct(y, x)
            # print(f"# dist_source {dist}, {y}, {x}")
            for i in range(4):
                ny = y + vy[i]
                nx = x + vx[i]
                if ny<0 or ny>=self.N or nx<0 or nx>=self.N: continue
                # 水源の隣に到達したら再計算してやり直す
                if self.field.is_source[ny][nx]:
                    print(f"# is_source {self.field.is_source[y][x]}, {ny}, {nx}")
                    self.field.init_dist_source()
                    return False
                if done[ny][nx]: continue
                cost = self.cost_function(ny, nx)
                heapq.heappush(h, (cost, ny, nx))
        return True

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
        # max_res = 5000
        # power = 100
        # power = self.C * 30   # sub01
        # power = int(math.log2(self.C) + 1.1) * 20   # sub02
        # power = int(math.log2(self.C) + 2.1) * 20 + 10   # sun03
        # power = int(math.log2(self.C) + 2.1) * 20 + 10
        power = int(math.log2(self.C) + 2.1) * 20 + self.field.min_sturdiness[y][x]
        # power = self.field.calc_expected_sturdiness(y, x)
        # power = min(self.field.calc_expected_sturdiness(y, x) * int(math.log2(self.C) + 2.1), 5000)
        # print(f"# power={power}, {y}, {x}")
        print(f"# ({y}, {x}) power={power} expected_sturdiness={self.field.calc_expected_sturdiness(y, x)}")
        while not self.field.is_broken[y][x]:
            result = self.field.query(y, x, power)
            if result == Response.FINISH:
                # for y in range(self.N):
                #     print(f"# dist_source {y}",  *self.field.dist_source[y], file=sys.stderr)
                print(f"total_cost={self.field.total_cost}", file=sys.stderr)
                sys.exit(0)
            elif result == Response.INVALID:
                print(f"invalid: y={y} x={x}", file=sys.stderr)
                sys.exit(1)
            # max_res -= power
            # power *= 2
            # power = (power - 10) * 2 + 10
            # power = min(power, max_res)
            power = min(power, self.field.max_sturdiness[y][x] - self.field.excavation[y][x])
        self.field.predict_sturdiness(y, x)


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
