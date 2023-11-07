# https://atcoder.jp/contests/abc322/tasks/abc322_d

# https://atcoder.jp/contests/abc322/submissions/46052401

N = 4

# ポリオミノをそれぞれsetに変換して、スライドさせる
def ConvertToSetAndThift(X, dy, dx):
    res = set()
    for i in range(N):
        for j in range(N):
            if X[i][j] == '#':
                res.add((i + dy, j + dx))
    return res

# ポリオミノを原点に移動させる
def normalize(S):
    x0 = min(x for x, y in S)
    y0 = min(y for x, y in S)
    return set((x - x0, y - y0) for x, y in S)

# ポリオミノを90度回転させる
def rotate(X):
    return list(zip(*X[::-1]))

# 入力
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]
C = [input() for _ in range(N)]

# 合計が16個でなければNo
if sum(row.count('#') for row in A + B + C) != N * N:
    print('No')
    exit()

# 16個のマスを全てカバーする集合
target = set()
for i in range(N):
    for j in range(N):
        target.add((i, j))

ans = False
# Aを固定して、BとCを回転，スライドさせる
for rotB in range(4):
    for rotC in range(4):
        for dyB in range(-N + 1, N):
            for dxB in range(-N + 1, N):
                for dyC in range(-N + 1, N):
                    for dxC in range(-N + 1, N):
                        setA = ConvertToSetAndThift(A, 0, 0)
                        setB = ConvertToSetAndThift(B, dyB, dxB)
                        setC = ConvertToSetAndThift(C, dyC, dxC)
                        # A, B, Cの和集合を原点に移動させたものがtargetと一致するか
                        ans |= normalize(setA | setB | setC) == target
        C = rotate(C)
    B = rotate(B)
print('Yes' if ans else 'No')


# TLE
# import numpy as np
# from itertools import product

# polyomino = np.array([[list(input()) for _ in range(4)] for _ in range(3)])
# polyomino = np.where(polyomino == '#', 1, 0)
# # print(polyomino.shape)
# # print(polyomino)
# # print(polyomino[2].shape)

# if polyomino.sum()!=16:
#     print("No")
#     exit()

# def rotate(p, k):
#     ret = p.copy()
#     for _ in range(k):
#         ret = np.rot90(ret)
#     return ret

# ans = False
# for i0, j0, i1, j1, i2, j2 in product(range(7), repeat=6):
#     # for r0, r1, r2 in product(range(4), repeat=3):
#     for r1, r2 in product(range(4), repeat=2):
#         # print(i0, j0, r0, i1, j1, r1, i2, j2, r2)
#         hex = np.zeros((10, 10), dtype=int)
#         # hex[i0:i0+4, j0:j0+4] += rotate(polyomino[0], r0)
#         hex[i0:i0+4, j0:j0+4] += polyomino[0]
#         hex[i1:i1+4, j1:j1+4] += rotate(polyomino[1], r1)
#         # print(rotate(polyomino[2], r2))
#         hex[i2:i2+4, j2:j2+4] += rotate(polyomino[2], r2)
#         if hex[3:7, 3:7].all() == 1:
#             ans = True
#             break
# if ans:
#     print("Yes")
# else:
#     print("No")
