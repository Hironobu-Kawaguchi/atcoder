import math
import random

def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

def lerp(a, b, x):
    return a + x * (b - a)

class PerlinNoise:
    def __init__(self, width=256, height=256):
        self.width = width
        self.height = height
        self.p = [i for i in range(256)]
        random.shuffle(self.p)
        self.p += self.p

    def noise(self, x, y):
        # Determine grid cell coordinates and wrap them for torus grid
        X = int(x) % self.width
        Y = int(y) % self.height
        x -= int(x)
        y -= int(y)
        
        u = fade(x)
        v = fade(y)

        # Hash coordinates
        a = self.p[X % 256] + Y
        b = self.p[(X + 1) % 256] + Y

        # And add blended results from 4 corners of the square
        return lerp(
            lerp(self.grad(self.p[a % 256], x, y), self.grad(self.p[b % 256], x-1, y), u),
            lerp(self.grad(self.p[(a + 1) % 256], x, y-1), self.grad(self.p[(b + 1) % 256], x-1, y-1), u),
            v
        )

    def grad(self, hash, x, y):
        h = hash & 15
        grad_x = 1 + (h & 7)  # Gradient value is one of 8 values
        grad_y = grad_x & 1
        return grad_x * x + grad_y * y

# # Test
# p = PerlinNoise(10, 10)
# for i in [x * 0.1 for x in range(15)]:  # Go beyond grid size to see torus effect
#     for j in [x * 0.1 for x in range(15)]:
#         print(p.noise(i, j))


# Define N and the grid 'h' (assuming it's a 2D list)
L = 50
h = [[0 for _ in range(L)] for _ in range(L)]

# Initialize the Perlin Noise generator (this is just an assumption based on the context)
perlin = PerlinNoise(L, L)

# Generate noise
# for (freq, amp) in [(random.uniform(2.0, 8.0), 1.0), (random.uniform(10.0, 20.0), 0.2)]:
for (freq, amp) in [(random.uniform(8.0, 8.0), 1.0), (random.uniform(20.0, 20.0), 0.2)]:
    y_offset = random.random()  # Generates a float between 0 and 1, similar to rng.gen::<f64>()
    x_offset = random.random()

    for r in range(L):
        for c in range(L):
            y = y_offset + r / L * freq
            x = x_offset + c / L * freq
            h[r][c] += perlin.noise(y, x) * amp  # Assuming 'noise' method exists in PerlinNoise class

max_value = 1000
min_value = 0
mx, mn = max(map(max, h)), min(map(min, h))

# Scale the noise to the desired range
for r in range(L):
    for c in range(L):
        h[r][c] = int((h[r][c] - mn) / (mx - mn) * (max_value - min_value) + min_value)

# Print the resulting grid (optional)
for row in h:
    print(*row)

print(-1, -1, -1)
for _ in range(95):
    print(1)
