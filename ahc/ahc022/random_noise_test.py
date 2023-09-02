import numpy as np

def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

def lerp(a, b, x):
    return a + x * (b - a)

def generate_perlin_noise_2d(shape, res):
    delta = (res[0] / shape[0], res[1] / shape[1])
    d = (shape[0] // res[0], shape[1] // res[1])
    gradient = np.random.randn(*res, 2)
    
    grid_x, grid_y = np.mgrid[0:shape[0], 0:shape[1]]
    grid_x = grid_x / shape[0]
    grid_y = grid_y / shape[1]
    grid_fx, grid_fy = grid_x * res[0] % 1, grid_y * res[1] % 1
    grid_ix = np.floor(grid_x * res[0]).astype(int) % res[0]
    grid_iy = np.floor(grid_y * res[1]).astype(int) % res[1]

    grad_x = gradient[grid_ix, grid_iy, 0]
    grad_y = gradient[grid_ix, grid_iy, 1]
    
    n00 = grad_x * grid_fx + grad_y * grid_fy
    n10 = grad_x * (grid_fx - 1) + grad_y * grid_fy
    n01 = grad_x * grid_fx + grad_y * (grid_fy - 1)
    n11 = grad_x * (grid_fx - 1) + grad_y * (grid_fy - 1)

    t = fade(grid_fx)
    n0 = lerp(n00, n10, t)
    n1 = lerp(n01, n11, t)

    t = fade(grid_fy)
    return lerp(n0, n1, t)

def generate_grid(L, max_value):
    # noise = generate_perlin_noise_2d((L, L), (4, 4))
    noise = generate_perlin_noise_2d((L, L), (L//4, L//4))
    noise = (noise - noise.min()) / (noise.max() - noise.min())
    return (max_value * noise).astype(int)

L = 50
max_value = 1000
grid = generate_grid(L, max_value)

for row in grid:
    print(*row)

print(-1, -1, -1)
for _ in range(95):
    print(1)
