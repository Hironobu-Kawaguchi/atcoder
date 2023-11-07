# 入力の大きさを定義
N = 50
M = 100

# 2Dリストの初期化用の関数
def make_2D(d1, d2, default_value):
    return [[default_value] * d2 for _ in range(d1)]

# Disjoint Set Union (DSU) クラス
class DSU:
    def __init__(self, n):
        self.rs = [0] * n
        self.ps = list(range(n))
        self.ss = [1] * n

    def find(self, x):
        if x != self.ps[x]:
            self.ps[x] = self.find(self.ps[x])
        return self.ps[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return
        if self.rs[xr] > self.rs[yr]:
            self.ps[yr] = xr
            self.ss[xr] += self.ss[yr]
        else:
            self.ps[xr] = yr
            if self.rs[xr] == self.rs[yr]:
                self.rs[yr] += 1
            self.ss[yr] += self.ss[xr]

    def size(self, x):
        return self.ss[self.find(x)]

# 行を削除する関数
def remove_row(r0, input_map):
    if all(cell <= 0 for cell in input_map[r0]):
        return None

    output_map = make_2D(len(input_map) - 1, len(input_map[0]), 0)
    for r, row in enumerate(input_map):
        if r < r0:
            output_map[r] = row.copy()
        elif r > r0:
            output_map[r - 1] = row.copy()
    return output_map

# 列を削除する関数
def remove_col(c0, input_map):
    if all(row[c0] <= 0 for row in input_map):
        return None

    output_map = make_2D(len(input_map), len(input_map[0]) - 1, 0)
    for r, row in enumerate(input_map):
        for c, cell in enumerate(row):
            if c < c0:
                output_map[r][c] = cell
            elif c > c0:
                output_map[r][c - 1] = cell
    return output_map

# 隣接マップを計算する関数
def compute_adjacent_map(input_map):
    h, w = len(input_map), len(input_map[0])
    output_adjacent_matrix = make_2D(M + 1, M + 1, 0)

    for r in range(h):
        for c in range(w):
            color_0 = input_map[r][c]
            if r + 1 < h and color_0 != input_map[r + 1][c]:
                color_1 = input_map[r + 1][c]
                output_adjacent_matrix[color_0][color_1] = 1
                output_adjacent_matrix[color_1][color_0] = 1
            if c + 1 < w and color_0 != input_map[r][c + 1]:
                color_1 = input_map[r][c + 1]
                output_adjacent_matrix[color_0][color_1] = 1
                output_adjacent_matrix[color_1][color_0] = 1

    return output_adjacent_matrix

# すべて接続されているかチェックする関数
def is_all_connected(input_map):
    color_exist = [0] * (M + 1)
    dsu = DSU((N + 2) * (N + 2))

    for r in range(N + 2):
        for c in range(N + 2):
            color_0 = input_map[r][c]
            color_exist[color_0] = 1

            if r + 1 < N + 2 and color_0 == input_map[r + 1][c]:
                dsu.union(r * (N + 2) + c, (r + 1) * (N + 2) + c)
            if c + 1 < N + 2 and color_0 == input_map[r][c + 1]:
                dsu.union(r * (N + 2) + c, r * (N + 2) + c + 1)

    if any(exist == 0 for exist in color_exist):
        return False

    root_count = sum(1 for i in range((N + 2) * (N + 2)) if dsu.find(i) == i)
    return root_count == M + 1

# 2つの行列が等しいかチェックする関数
def is_equal_matrix(matrix_0, matrix_1):
    return all(r1 == r2 for r1, r2 in zip(matrix_0, matrix_1))

# メイン関数
def main():
    unused_n, unused_m = map(int, input().split())

    original_map = make_2D(N + 2, N + 2, 0)
    for r in range(1, N + 1):
        original_map[r][1:N+1] = list(map(int, input().split()))

    original_adjacent_matrix = compute_adjacent_map(original_map)

    current_map = original_map.copy()
    while True:
        updated = False
        for r0 in range(1, N + 1):
            candidate_map = remove_row(r0, current_map)
            if candidate_map is None:
                continue
            candidate_adjacent_matrix = compute_adjacent_map(candidate_map)
            if is_all_connected(candidate_map) and is_equal_matrix(original_adjacent_matrix, candidate_adjacent_matrix):
                current_map = candidate_map
                updated = True

        for c0 in range(1, N + 1):
            candidate_map = remove_col(c0, current_map)
            if candidate_map is None:
                continue
            candidate_adjacent_matrix = compute_adjacent_map(candidate_map)
            if is_all_connected(candidate_map) and is_equal_matrix(original_adjacent_matrix, candidate_adjacent_matrix):
                current_map = candidate_map
                updated = True

        if not updated:
            break

    for row in current_map[1:N+1]:
        print(" ".join(map(str, row[1:N+1])))

# 実行
if __name__ == "__main__":
    main()
