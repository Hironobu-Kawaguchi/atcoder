# https://atcoder.jp/contests/ahc022/tasks/ahc022_a
from typing import List
import sys
import math
import numpy as np
import random
import time
time_start = time.time()

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
        self.interval = min(self.S + 1, 1000 // (self.N - 1))        # 配置間隔: Sが小さい時は小さい間隔でコストを抑える
        # self.max_temperture = 1000
        self.max_temperture = min(1000, self.S * 2)
        self.measure_count = min(10000 // self.N, math.ceil((1.0 * self.z * self.S / self.interval) ** 2) + 0)        # 計測回数
        print(f"pass_flg={self.pass_flg} interval={self.interval} measure_count={self.measure_count}", file=sys.stderr)

    def solve(self) -> None:
        temperature = self._create_temperature()
        self.judge.set_temperature(temperature)
        estimate = self._predict(temperature)
        self.judge.answer(estimate)

    def _create_temperature(self) -> List[List[int]]:
        temperature = [[0] * self.L for _ in range(self.L)]
        if self.pass_flg:
            for x in range(self.L):
                for y in range(self.L):
                    temperature[y][x] = random.randint(0, self.max_temperture)
            return temperature
        # set the temperature to i * 10 for i-th position
        for i, pos in enumerate(self.landing_pos):
            # temperature[pos.y][pos.x] = i * 10
            if self.interval == 1000 // (self.N - 1):
                temperature[pos.y][pos.x] = int(i * 1000 / (self.N - 1))
            else:
                temperature[pos.y][pos.x] = i * self.interval

        # if self.pass_flg:
        #     for x in range(self.L):
        #         for y in range(self.L):
        #             if not self.landing[y][x]:
        #                 temperature[y][x] = random.randint(0, 1000)
        #     return temperature

        # Perform 2D Laplacian smoothing on a grid.
        # iterations=1000
        iterations=300
        for _ in range(iterations):
            for x in range(self.L):
                for y in range(self.L):
                    if not self.landing[y][x]:
                        temperature[y][x] = (temperature[(y+1)%self.L][x] + temperature[(y-1+self.L)%self.L][x] + temperature[y][(x+1)%self.L] + temperature[y][(x-1+self.L)%self.L]) // 4
        return temperature

    def _predict(self, temperature: List[List[int]]) -> List[int]:
        if self.pass_flg:
            # log_likelihood = np.zeros((self.N, self.N), dtype=np.float64)
            log_likelihood = np.zeros((self.N, self.N), dtype=np.int64)
            warmup = 0
            max_dist = 7
            move_list = []
            for dist in range(1, max_dist+1):
                for _y in range(dist+1):
                    for y_sign in range(2):
                        if _y==0 and y_sign==1: continue
                        y = _y if y_sign==0 else -_y
                        for x_sign in range(2):
                            if _y==dist and x_sign==1: continue
                            x = dist - _y if x_sign==0 else -dist + _y
                            move_list.append((y, x))
            for iter in range(10000//self.N):
                for i_in in range(self.N):
                    # if iter < warmup:
                    #     y, x = 0, 0
                    # else:
                    #     # size = 5
                    #     size = 7
                    #     y = ((iter+warmup+((size//2)*size+size//2))%(size*size)) //size - size//2
                    #     x = ((iter+warmup+((size//2)*size+size//2))%(size*size)) % size - size//2
                    y, x = move_list[iter%len(move_list)]
                    m = self.judge.measure(i_in, y, x)
                    for i_out in range(self.N):
                        # log_likelihood[i_in][i_out] += (m - temperature[(self.landing_pos[i_out].y + y + self.L)%self.L][(self.landing_pos[i_out].x + x + self.L)%self.L])**2 / (self.S)**2
                        log_likelihood[i_in][i_out] += (m - temperature[(self.landing_pos[i_out].y + y + self.L)%self.L][(self.landing_pos[i_out].x + x + self.L)%self.L])**2
                estimate = np.argmin(log_likelihood, axis=1).tolist()
                if len(set(estimate)) == self.N:
                    break
            # return list(range(self.N))
            return estimate
        estimate = [-1] * self.N
        count = 0
        measured_values = [[] for _ in range(self.N)]
        for i_in in range(self.N):
            # for j in range(int(2*self.S**0.5+0.1)):
            for j in range(self.measure_count):
                measured_values[i_in].append(self.judge.measure(i_in, 0, 0))
                count += 1
        # for i_in in range(self.N):
        #     while max(measured_values[i_in]) - min(measured_values[i_in]) < self.S:
        #         measured_values[i_in].append(self.judge.measure(i_in, 0, 0))
        #         count += 1

        # answer the position with the temperature closest to the measured value
        while time.time() - time_start < 3.5:
            measured_values_mean = [(np.mean(v), i_in) for i_in, v in enumerate(measured_values)]
            measured_values_mean.sort()
            for i in range(self.N - 1):
                if count>=10000: break
                if measured_values_mean[i+1][0] - measured_values_mean[i][0] < self.interval * 0.5:
                    if len(measured_values[measured_values_mean[i][1]]) < len(measured_values[measured_values_mean[i+1][1]]):
                        i_in = measured_values_mean[i][1]
                    else:
                        i_in = measured_values_mean[i+1][1]
                    measured_values[i_in].append(self.judge.measure(i_in, 0, 0))
                    count += 1
                    if count>=10000: break
            if count>=10000: break

        for i, (v, i_in) in enumerate(measured_values_mean):
            estimate[i_in] = i
            print(f"# i_in={i_in} measured value mean={v:.1f} i={i} count={len(measured_values[i_in])}")
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
