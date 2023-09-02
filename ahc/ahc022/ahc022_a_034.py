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


def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

def lerp(a, b, x):
    return a + x * (b - a)

class PerlinNoise:
    def __init__(self, size=256):
        self.size = size
        self.p = [i for i in range(256)]
        random.shuffle(self.p)
        self.p += self.p

    def noise(self, x, y):
        # Determine grid cell coordinates and wrap them for torus grid
        X = int(x) % self.size
        Y = int(y) % self.size
        x -= int(x)
        y -= int(y)
        
        u = fade(x)
        v = fade(y)

        # Hash coordinates
        a = self.p[X % self.size] + Y
        b = self.p[(X + 1) % self.size] + Y

        # And add blended results from 4 corners of the square
        return lerp(
            lerp(self.grad(self.p[a % self.size], x, y), self.grad(self.p[b % self.size], x-1, y), u),
            lerp(self.grad(self.p[(a + 1) % self.size], x, y-1), self.grad(self.p[(b + 1) % self.size], x-1, y-1), u),
            v
        )

    def grad(self, hash, x, y):
        h = hash & 15
        grad_x = 1 + (h & 7)  # Gradient value is one of 8 values
        grad_y = grad_x & 1
        return grad_x * x + grad_y * y


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
        self.pass_flg = self.S > 2 * 10**5 / (self.z * self.N**1.5)  # Sが大きいと推測不可能なので，コストを0に抑える
        # self.interval = min(self.S + 1, 1000 // (self.N - 1))        # 配置間隔: Sが小さい時は小さい間隔でコストを抑える
        # self.max_temperture = 1000
        # self.max_temperture = max(min(1000, int(self.S * 4.0)), 50)
        # self.max_temperture = max(min(1000, int(self.S * 3.0)), 64)
        self.max_temperture = min(1000, int(self.S * 2.0) + 30)
        # self.max_temperture = min(1000, int(int(self.S**(1/3)+0.1) * 32.0))
        # self.measure_count = min(10000 // self.N, math.ceil((1.0 * self.z * self.S / self.interval) ** 2) + 0)        # 計測回数
        # print(f"pass_flg={self.pass_flg} interval={self.interval} measure_count={self.measure_count}", file=sys.stderr)
        print(f"pass_flg={self.pass_flg} max_temperture={self.max_temperture}", file=sys.stderr)

    def solve(self) -> None:
        temperature = self._create_temperature()
        self.judge.set_temperature(temperature)
        estimate = self._predict(temperature)
        self.judge.answer(estimate)


    def generate_noise_grid(self, max_value=1000):
        # Define N and the grid 'h' (assuming it's a 2D list)
        # result = [[0 for _ in range(self.L)] for _ in range(self.L)]
        result = [[random.random() for _ in range(self.L)] for _ in range(self.L)]

        # if not self.pass_flg:
        #     # Generate noise
        #     noise_list = [
        #         # (random.uniform(0,          self.L//2),  0.1),
        #         # (random.uniform(0,          self.L//4),  0.2),
        #         # (random.uniform(0,          self.L//8),  0.4),
        #         # (random.uniform(0,          self.L//16), 0.8),
        #         # (random.uniform(self.L,     self.L*2),   0.1),
        #         # (random.uniform(self.L//2,  self.L),     0.2),
        #         # (random.uniform(self.L//4,  self.L//2),  0.4),
        #         # (random.uniform(self.L//4,  self.L//2),  0.8),
        #         # (random.uniform(self.L//4,  self.L//2),  1/self.S),
        #         (random.uniform(self.L//4,  self.L//2),  1/(self.S**0.5)),
        #         # (random.uniform(self.L//8,  self.L//4),  0.8),
        #         # (random.uniform(self.L//16, self.L//8),  0.8),
        #         # (random.uniform(self.L//32, self.L//16), 1.6),
        #         ]
        #     # for (freq, amp) in [(random.uniform(2.0, 8.0), 1.0), (random.uniform(10.0, 20.0), 0.2)]:
        #     for (freq, amp) in noise_list:
        #         # Initialize the Perlin Noise generator (this is just an assumption based on the context)
        #         perlin = PerlinNoise(self.L)

        #         y_offset = random.random()  # Generates a float between 0 and 1, similar to rng.gen::<f64>()
        #         x_offset = random.random()

        #         for r in range(self.L):
        #             for c in range(self.L):
        #                 y = y_offset + r / self.L * freq
        #                 # x = x_offset + c / self.L * freq
        #                 x = x_offset + c / self.L * freq * 2
        #                 result[r][c] += perlin.noise(y, x) * amp  # Assuming 'noise' method exists in PerlinNoise class

        mx, mn = max(map(max, result)), min(map(min, result))

        # Scale the noise to the desired range
        for r in range(self.L):
            for c in range(self.L):
                result[r][c] = int((result[r][c] - mn) / (mx - mn) * (self.max_temperture - 0) + 0)
        
        return result

    def _create_temperature(self) -> List[List[int]]:
        return self.generate_noise_grid(self.max_temperture)
        # temperature = [[0] * self.L for _ in range(self.L)]
        # for x in range(self.L):
        #     for y in range(self.L):
        #         temperature[y][x] = random.randint(0, self.max_temperture)
        # return temperature

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
