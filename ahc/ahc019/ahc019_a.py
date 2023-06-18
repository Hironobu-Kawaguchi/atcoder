# https://atcoder.jp/contests/ahc019/tasks/ahc019_a

import sys
from collections import deque
import numpy as np
from scipy import ndimage

vx = [0, 1, 0, -1, 0, 0]
vy = [1, 0, -1, 0, 0, 0]
vz = [0, 0, 0, 0, 1, -1]

D = int(input())
f = [[] for i in range(2)]
r = [[] for i in range(2)]
for i in range(2):
    for k in range(D):
        f[i].append(input())
    for k in range(D):
        r[i].append(input())

def xyz2idx(x, y, z):
    return x * D * D + y * D + z

def idx2xyz(idx):
    z = idx % D
    idx = idx // D
    y = idx % D
    idx = idx // D
    x = idx % D
    return x, y, z

# 1つのマスについて、そのマスの上下左右に1があるかどうかを調べる
def check(i, x, y, z):
    flgx = False
    for xx in range(D):
        if xx==x: continue
        if b[i][xx * D * D + y * D + z] > 0:
            flgx = True
            break
    flgy = False
    for yy in range(D):
        if yy==y: continue
        if b[i][x * D * D + yy * D + z] > 0:
            flgy = True
            break
    return flgx and flgy

b = [[0 for j in range(D * D * D)] for i in range(2)]
n = 0
nn = [0]*2
for i in range(2):
    for x in range(D):
        for y in range(D):
            for z in range(D):
                if f[i][z][x] == '1' and r[i][z][y] == '1':
                    if check(i, x, y, z): continue
                    n += 1
                    b[i][xyz2idx(x, y, z)] = n
    nn[i] = n

def rotate_shift_zero_largest_common(a, b):
    def rotate(matrix, axis, k):
        if axis == "x":
            return np.rot90(matrix, k=k, axes=(1, 2))
        elif axis == "y":
            return np.rot90(matrix, k=k, axes=(0, 2))
        elif axis == "z":
            return np.rot90(matrix, k=k, axes=(0, 1))
        else:
            raise ValueError("Invalid axis")

    # def shift(matrix, axis, amount):
    #     return np.roll(matrix, shift=amount, axis=axis)
    def shift(matrix, axis, amount):
        shifted_matrix = np.roll(matrix, shift=amount, axis=axis)
        
        if amount > 0:
            if axis == 0:
                shifted_matrix[:amount, :, :] = 0
            elif axis == 1:
                shifted_matrix[:, :amount, :] = 0
            elif axis == 2:
                shifted_matrix[:, :, :amount] = 0
        elif amount < 0:
            if axis == 0:
                shifted_matrix[amount:, :, :] = 0
            elif axis == 1:
                shifted_matrix[:, amount:, :] = 0
            elif axis == 2:
                shifted_matrix[:, :, amount:] = 0
                
        return shifted_matrix

    # def find_largest_connected_component(arr):
    #     structure = ndimage.generate_binary_structure(3, 1)
    #     labeled, num_features = ndimage.label(arr, structure=structure)
    #     sizes = ndimage.sum(arr, labeled, range(1, num_features + 1))
    #     if sizes.size == 0:
    #         return None, None, 0
    #     largest_component_label = np.argmax(sizes) + 1
    #     return labeled == largest_component_label, largest_component_label, sizes[largest_component_label - 1]

    def find_largest_connected_component(arr):
        # 面のみ接続された図形を連結成分として認識する構造要素
        structure = np.array([[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
                            [[0, 1, 0], [1, 0, 1], [0, 1, 0]],
                            [[0, 0, 0], [0, 1, 0], [0, 0, 0]]], dtype=bool)

        labeled, num_features = ndimage.label(arr, structure=structure)
        sizes = ndimage.sum(arr, labeled, range(1, num_features + 1))
        if sizes.size == 0:
            return None, None, 0
        largest_component_label = np.argmax(sizes) + 1
        return labeled == largest_component_label, largest_component_label, sizes[largest_component_label - 1]

    axes = ["x", "y", "z"]
    rotations = [0, 1, 2, 3]  # 0, 90, 180, 270 degrees
    # shifts = [0]
    # shifts = [-2, -1, 0, 1, 2]
    shifts = list(range(-D+1, D))
    largest_component = None
    largest_component_label = None
    largest_component_size = 0
    best_rotation = None
    best_shift = None

    for axis in axes:
        for k in rotations:
            a_rotated = rotate(a, axis, k)
            for axis_shift in range(3):  # x, y, z axes
                for shift_amount in shifts:
                    a_shifted = shift(a_rotated, axis_shift, shift_amount)
                    common_area = (a_shifted > 0) & (b > 0)
                    connected_component, component_label, component_size = find_largest_connected_component(common_area)
                    if connected_component is not None:
                        if component_size > largest_component_size:
                            largest_component_size = component_size
                            largest_component = connected_component
                            largest_component_label = component_label
                            best_rotation = (axis, k)
                            best_shift = (axis_shift, shift_amount)

    if largest_component is not None and largest_component_size > 1:
        # a_rotated = rotate(a, best_rotation[0], best_rotation[1])
        # a_shifted = shift(a_rotated, best_shift[0], best_shift[1])
        largest_component_rotated = shift(largest_component, best_shift[0], -best_shift[1])
        largest_component_shifted = rotate(largest_component_rotated, best_rotation[0], -best_rotation[1])
        common_a_indices = np.where(largest_component_shifted)
        # common_a_indices = np.where(largest_component)
        common_b_indices = np.where(largest_component)

        # edited_values_a = set(a_shifted[common_a_indices])
        edited_values_a = set(a[common_a_indices])
        edited_values_b = set(b[common_b_indices])

        # a_shifted[common_a_indices] = 0
        a[common_a_indices] = 0
        b[common_b_indices] = 0

        # a = shift(a_shifted, best_shift[0], -best_shift[1])
        # a = rotate(a, best_rotation[0], -best_rotation[1])
    else:
        return a, b, set(), set(), None, 0

    return a, b, edited_values_a, edited_values_b, largest_component, largest_component_size

def make_map(a0, a1):
    # n個の割り当てリスト作成
    mp = [-1] * (n+1)
    mp[0] = 0
    cnt = 0

    while True:
        cnt += 1
        a0, a1, edited_values_a, edited_values_b, largest_component, largest_component_size = rotate_shift_zero_largest_common(a0, a1)
        for k in edited_values_a:
            if mp[k]!=-1:
                print("error", k, mp[k], cnt, file=sys.stderr)
            mp[k] = cnt
        for k in edited_values_b:
            if mp[k]!=-1:
                print("error", k, mp[k], cnt, file=sys.stderr)
            mp[k] = cnt
        # print("#", cnt, largest_component_size, edited_values_a, edited_values_b)
        if largest_component_size == 0:
            cnt -= 1
            break
        if np.all(a0 == 0) or np.all(a1 == 0):
            break

    ii = [0, 0]
    a = [a0, a1]
    while True:
        cnt += 1
        flg = [False, False]
        for i in range(2):
            for j in range(ii[i], D*D*D):
                x, y, z = idx2xyz(j)
                if a[i][x,y,z]>0 and mp[a[i][x,y,z]]==-1:
                    ii[i] = j
                    mp[a[i][x,y,z]] = cnt
                    break
            else:
                flg[i] = True
        if flg[0] and flg[1]: break
    return mp, cnt - 1

a0 = np.array(b[0]).reshape(D, D, D)
a1 = np.array(b[1]).reshape(D, D, D)
mp, cnt = make_map(a0, a1)

print(cnt)
print(' '.join(map(str, [mp[x] for x in b[0]])))
print(' '.join(map(str, [mp[x] for x in b[1]])))
