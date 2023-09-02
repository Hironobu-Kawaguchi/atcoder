# https://atcoder.jp/contests/ahc022/tasks/ahc022_a
from typing import List
import sys
import math
import numpy as np


class Pos:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x


class Judge:
    def set_temperature(self, temperature: List[List[int]]) -> None:
        for row in temperature:
            print(" ".join(map(str, row)))
        sys.stdout.flush()

    def measure(self, i: int, y: int, x: int) -> int:
        print(f"{i} {y} {x}", flush=True)
        v = int(input())
        print(f"# measure i={i} y=0 x=0 -> {v}")

        if v == -1:
            print(f"something went wrong. i={i} y={y} x={x}", file=sys.stderr)
            sys.exit(1)
        return v

    def answer(self, estimate: List[int]) -> None:
        print("-1 -1 -1")
        for e in estimate:
            print(e)
        sys.stdout.flush()

class Solver:

    def __init__(self, L: int, N: int, S: int, landing_pos: List[Pos], landing: List[List[bool]]):
        self.L = L
        self.N = N
        self.S = S
        self.landing_pos = landing_pos
        self.landing = landing
        self.judge = Judge()
        # self.z = 1.96   # 95% confidence interval
        self.z = 2.58   # 99% confidence interval
        self.pass_flg = self.S > 2 * 10**5 / (self.z * self.N**1.5)  # Sが大きいと推測不可能なので，コストを0に抑える
        self.interval = min(self.S + 2, 1000 // (self.N - 1))        # 配置間隔: Sが小さい時は小さい間隔でコストを抑える
        self.measure_count = min(10000 // self.N, math.ceil((1.5 * self.z * self.S / self.interval) ** 2) + 0)        # 計測回数
        print(f"pass_flg={self.pass_flg} interval={self.interval} measure_count={self.measure_count}", file=sys.stderr)

    def solve(self) -> None:
        temperature = self._create_temperature()
        self.judge.set_temperature(temperature)
        estimate = self._predict(temperature)
        self.judge.answer(estimate)

    def _create_temperature(self) -> List[List[int]]:
        temperature = [[0] * self.L for _ in range(self.L)]
        if self.pass_flg:
            return temperature
        # set the temperature to i * 10 for i-th position
        for i, pos in enumerate(self.landing_pos):
            # temperature[pos.y][pos.x] = i * 10
            if self.interval == 1000 // (self.N - 1):
                temperature[pos.y][pos.x] = int(i * 1000 / (self.N - 1))
            else:
                temperature[pos.y][pos.x] = i * self.interval

        # Perform 2D Laplacian smoothing on a grid.
        iterations=1000
        for _ in range(iterations):
            for x in range(self.L):
                for y in range(self.L):
                    if not self.landing[y][x]:
                        temperature[y][x] = (temperature[(y+1)%self.L][x] + temperature[(y-1+self.L)%self.L][x] + temperature[y][(x+1)%self.L] + temperature[y][(x-1+self.L)%self.L]) // 4
        return temperature

    def _predict(self, temperature: List[List[int]]) -> List[int]:
        if self.pass_flg:
            return list(range(self.N))
        estimate = [-1] * self.N
        measured_values = [[] for _ in range(self.N)]
        for i_in in range(self.N):
            for j in range(self.measure_count):
                measured_values[i_in].append(self.judge.measure(i_in, 0, 0))

        # answer the position with the temperature closest to the measured value
        measured_values_mean = [(np.mean(v), i) for i, v in enumerate(measured_values)]
        measured_values_mean.sort()
        for i, (v, i_in) in enumerate(measured_values_mean):
            estimate[i_in] = i
            print(f"# i_in={i_in} measured value mean={v:.1f} i={i}")
        # for i_in in range(self.N):
        #     min_diff = 9999
        #     for i_out, pos in enumerate(self.landing_pos):
        #         diff = abs(temperature[pos.y][pos.x] - measured_value)
        #         if diff < min_diff:
        #             min_diff = diff
        #             estimate[i_in] = i_out
        return estimate


def main():
    L, N, S = [int(v) for v in input().split(" ")]
    print(f"L={L} N={N} S={S}", file=sys.stderr)
    landing_pos = []
    landing = [[False] * L for _ in range(L)]
    for _ in range(N):
        y, x = (int(v) for v in input().split(" "))
        landing_pos.append(Pos(y, x))
        landing[y][x] = True

    solver = Solver(L, N, S, landing_pos, landing)
    solver.solve()


if __name__ == "__main__":
    main()
