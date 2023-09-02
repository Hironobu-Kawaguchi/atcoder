# https://atcoder.jp/contests/ahc022/tasks/ahc022_a
from typing import List
import sys
import math
import numpy as np
from scipy import interpolate
import random
import time

time_start = time.time()
SEED = 1234
random.seed(SEED)
np.random.seed(SEED)


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
        print(f"# measure i={i} y={y} x={x} -> {v}")

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
        # self.pass_flg = self.S > 2 * 10**5 / (self.z * self.N**1.5)  # Sが大きいと推測不可能なので，コストを0に抑える
        self.pass_flg = self.S > 10**5 / (self.z * self.N**1.5)  # Sが大きいと推測不可能なので，コストを0に抑える
        # self.interval = min(self.S + 1, 1000 // (self.N - 1))        # 配置間隔: Sが小さい時は小さい間隔でコストを抑える
        # self.interval = min(self.S * 5, 1000)        # 配置間隔: Sが小さい時は小さい間隔でコストを抑える
        self.interval = min(math.ceil(self.S * 1.5), 1000)        # 配置間隔: Sが小さい時は小さい間隔でコストを抑える
        # self.interval_num = 1000 // self.interval + 1 if self.interval > 64 else 64 // self.interval + 1   # 10箇所取れば，2回の計測で10^2==100通りを判別可能，３回で10^3==1000通りを判別可能
        self.interval_num = 2 if self.interval > 20 else 32 // self.interval + 1   # 10箇所取れば，2回の計測で10^2==100通りを判別可能，３回で10^3==1000通りを判別可能
        # self.max_temperture = 1000
        self.max_temperture = max(min(1000, int(self.S * 6.0)), 50)
        # self.max_temperture = min(1000, int(int(self.S**(1/3)+0.1) * 32.0))
        # self.measure_count = min(10000 // self.N, math.ceil((1.0 * self.z * self.S / self.interval) ** 2) + 0)        # 計測回数
        # print(f"pass_flg={self.pass_flg} interval={self.interval} measure_count={self.measure_count}", file=sys.stderr)
        # print(f"pass_flg={self.pass_flg} max_temperture={self.max_temperture}", file=sys.stderr)
        print(f"pass_flg={self.pass_flg}, max_temperture={self.max_temperture} interval={self.interval} interval_num={self.interval_num}", file=sys.stderr)

    def solve(self) -> None:
        temperature = self._create_temperature()
        self.judge.set_temperature(temperature)
        estimate = self._predict(temperature)
        self.judge.answer(estimate)

    def _create_temperature(self) -> List[List[int]]:
        if self.pass_flg:
            result = [[0 for _ in range(self.L)] for _ in range(self.L)]
            for y in range(self.L):
                for x in range(self.L):
                    result[y][x] = random.randint(0, self.interval_num - 1) * self.interval
            return result
        else:
            # より小さなランダムグリッドを生成
            scale_factor = self.L // 2  # この値を変更すると、ノイズの特性が変わります
            # scale_factor = int(self.L * 0.4)  # この値を変更すると、ノイズの特性が変わります
            small_grid = np.random.randint(0, self.max_temperture + 1, size=(scale_factor, scale_factor))
            
            # トーラス状にするための準備
            small_grid = np.vstack((small_grid, small_grid[0, :]))
            small_grid = np.hstack((small_grid, small_grid[:, 0][:, np.newaxis]))

            # interpolateを使用してグリッドをアップスケール
            x = np.linspace(0, 1, scale_factor + 1)
            y = np.linspace(0, 1, scale_factor + 1)
            f = interpolate.interp2d(x, y, small_grid, kind='cubic')
            
            x_upscaled = np.linspace(0, 1, self.L)
            y_upscaled = np.linspace(0, 1, self.L)
            upscaled_grid = f(x_upscaled, y_upscaled)

            # 値の範囲を整数に調整
            upscaled_grid = np.round(upscaled_grid).astype(int)
            upscaled_grid = np.clip(upscaled_grid, 0, self.max_temperture)
            
            # numpy配列をPythonのリストに変換
            result = upscaled_grid.tolist()
            
            return result


    def _predict(self, temperature: List[List[int]]) -> List[int]:
        log_likelihood = np.zeros((self.N, self.N), dtype=np.int64)
        warmup = 0
        max_dist = 8
        # max_dist = 7
        # max_dist = 6
        # max_dist = 5
        move_list = []
        for dist in range(max_dist+1):
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
                y, x = move_list[iter%len(move_list)]
                m = self.judge.measure(i_in, y, x)
                for i_out in range(self.N):
                    log_likelihood[i_in][i_out] += (m - temperature[(self.landing_pos[i_out].y + y + self.L)%self.L][(self.landing_pos[i_out].x + x + self.L)%self.L])**2
            estimate = np.argmin(log_likelihood, axis=1).tolist()
            if len(set(estimate)) == self.N:
                break
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
