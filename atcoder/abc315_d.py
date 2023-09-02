# https://atcoder.jp/contests/abc315/tasks/abc315_d
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

# 入力を受け取る
h, w = map(int, input().split())

# グリッドを読み込む
c = [list(input()) for _ in range(h)]

# 各行・各列での各アルファベットの出現数をカウントする2Dリスト
x = [[0] * 26 for _ in range(h)]
y = [[0] * 26 for _ in range(w)]

# 各アルファベットの出現数をカウント
for i in range(h):
    for j in range(w):
        x[i][ord(c[i][j]) - ord('a')] += 1
        y[j][ord(c[i][j]) - ord('a')] += 1

hc, wc = h, w
fx, fy = [False] * h, [False] * w

# 各行・各列を調べ、条件を満たす行・列を削除する
for _ in range(h + w):
    ux, uy = [], []
    
    for i in range(h):
        if fx[i]: continue
        for j in range(26):
            if x[i][j] == wc and wc >= 2:
                ux.append((i, j))
                
    for i in range(w):
        if fy[i]: continue
        for j in range(26):
            if y[i][j] == hc and hc >= 2:
                uy.append((i, j))
                
    for p in ux:
        fx[p[0]] = True
        for i in range(w):
            y[i][p[1]] -= 1
        hc -= 1
        
    for p in uy:
        fy[p[0]] = True
        for i in range(h):
            x[i][p[1]] -= 1
        wc -= 1

# 残っているセルの数を出力
print(hc * wc)



# TLE
# import sys
# # input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# # sys.setrecursionlimit(10 ** 7)

# H, W = map(int, input().split())
# c = [list(input()) for _ in range(H)]
# # print(c, file=sys.stderr)

# flg_h, flg_w = [False]*H, [False]*W
# while True:
#     st_h, st_w = set(), set()
#     for i in range(H):
#         if flg_h[i]: continue
#         ch = ''
#         cnt = 0
#         flg = True
#         for j in range(W):
#             if flg_w[j]: continue
#             if ch != '' and c[i][j] != ch:
#                 flg = False
#                 break
#             ch = c[i][j]
#             cnt += 1
#         if flg and cnt>=2:
#             st_h.add(i)
#     for j in range(W):
#         if flg_w[j]: continue
#         ch = ''
#         cnt = 0
#         flg = True
#         for i in range(H):
#             if flg_h[i]: continue
#             if ch != '' and c[i][j] != ch:
#                 flg = False
#                 break
#             ch = c[i][j]
#             cnt += 1
#         if flg and cnt>=2:
#             st_w.add(j)
#     if len(st_h)==0 and len(st_w)==0:
#         break
#     for i in st_h:
#         flg_h[i] = True
#     for j in st_w:
#         flg_w[j] = True
#     # print(st_h, st_w, file=sys.stderr)

# ans = 0
# result = [['']*W for _ in range(H)]
# for i in range(H):
#     for j in range(W):
#         if flg_h[i] or flg_w[j]:
#             result[i][j] = '.'
#         else:
#             ans += 1
#             result[i][j] = c[i][j]
# # for i in range(H):
# #     print(''.join(result[i]), file=sys.stderr)
# print(ans)
