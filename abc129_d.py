# 
# https://atcoder.jp/contests/abc129/tasks/abc129_d

# https://atcoder.jp/contests/abc129/submissions/5850116
# import numpy as np
# import sys
# import os

# if os.getenv("LOCAL"):
#     sys.stdin = open("_in.txt", "r")

# sys.setrecursionlimit(2147483647)
# INF = float("inf")

# H, W = list(map(int, sys.stdin.readline().split()))

# S = np.array([list(sys.stdin.readline().rstrip()) for _ in range(H)]) == '.'
# ups = np.zeros((H, W), dtype=int)
# downs = np.zeros((H, W), dtype=int)
# rights = np.zeros((H, W), dtype=int)
# lefts = np.zeros((H, W), dtype=int)

# for h in range(1, H):
#     ups[h] = (ups[h - 1] + 1) * S[h - 1]
# for h in reversed(range(H - 1)):
#     downs[h] = (downs[h + 1] + 1) * S[h + 1]
# for w in range(1, W):
#     lefts[:, w] = (lefts[:, w - 1] + 1) * S[:, w - 1]
# for w in reversed(range(W - 1)):
#     rights[:, w] = (rights[:, w + 1] + 1) * S[:, w + 1]
# print(((ups + downs + lefts + rights) * S).max() + 1)



import numpy as np
H, W = map(int, input().split())
S = []
ij = np.zeros((H,W), dtype=int)    # .の連続数を格納用

for i in range(H):
    S.append(input())
    cnt = 0
    start = 0
    end = 0
    for j in range(W):
        if S[i][j] == '#':
            ij[i, start:end+1] += cnt
            cnt = 0
        elif j > 0 and S[i][j-1] == '#':    # .のstart
            start = j
            end = j
            cnt = 1
        else:
            end = j
            cnt += 1
        if j == W-1:    # 最後に書き込み
            ij[i, start:end+1] += cnt
            cnt = 0

for j in range(W):
    cnt = 0
    start = 0
    end = 0
    for i in range(H):
        if S[i][j] == '#':
            ij[start:end+1, j] += cnt
            cnt = 0
        elif i > 0 and S[i-1][j] == '#':    # .のstart
            start = i
            end = i
            cnt = 1
        else:
            end = i
            cnt += 1
        if i == H-1:    # 最後に書き込み
            ij[start:end+1, j] += cnt
            cnt = 0

ij = ij - 1  # 自分が2回足されるので、1引く
ans = ij.max()
print(ans)



# import numpy as np
# H, W = map(int, input().split())
# S = [input() for _ in range(H)]

# ij = np.zeros([H,W])    # 横の.の連続数を格納用
# ji = np.zeros([H,W])    # 縦の.の連続数を格納用

# for i in range(H):
#     cnt = 0
#     start = 0
#     end = 0
#     for j in range(W):
#         if S[i][j] == '#':
#             ij[i, start:end+1] += cnt
#             cnt = 0
#         elif j > 0 and S[i][j-1] == '#':    # .のstart
#             start = j
#             end = j
#             cnt = 1
#         else:
#             end = j
#             cnt += 1
#         if j == W-1:    # 最後に書き込み
#             ij[i, start:end+1] += cnt
#             cnt = 0

# for j in range(W):
#     cnt = 0
#     start = 0
#     end = 0
#     for i in range(H):
#         if S[i][j] == '#':
#             ji[start:end+1, j] += cnt
#             cnt = 0
#         elif i > 0 and S[i-1][j] == '#':    # .のstart
#             start = i
#             end = i
#             cnt = 1
#         else:
#             end = i
#             cnt += 1
#         if i == H-1:    # 最後に書き込み
#             ji[start:end+1, j] += cnt
#             cnt = 0

# iijj = ij + ji - 1  # 自分が2回足されるので、1引く
# # print(iijj)
# ans = int(iijj.max())
# print(ans)
    


# H, W = map(int, input().split())
# S = [input() for _ in range(H)]

# ans = 0
# for i in range(H):
#     for j in range(W):
#         if S[i][j] == '#':
#             continue
#         else:
#             cnt = 1 # 光の数 自分も含む

#             flg = True
#             k = 1
#             while flg:
#                 if i-k < 0:
#                     flg = False
#                     break
#                 else:
#                     if S[i-k][j] == '#':
#                         flg = False
#                         break
#                     else:
#                         cnt += 1
#                 k += 1

#             flg = True
#             k = 1
#             while flg:
#                 if j-k < 0:
#                     flg = False
#                     break
#                 else:
#                     if S[i][j-k] == '#':
#                         flg = False
#                         break
#                     else:
#                         cnt += 1
#                 k += 1

#             flg = True
#             k = 1
#             while flg:
#                 if i+k >= H:
#                     flg = False
#                     break
#                 else:
#                     if S[i+k][j] == '#':
#                         flg = False
#                         break
#                     else:
#                         cnt += 1
#                 k += 1

#             flg = True
#             k = 1
#             while flg:
#                 if j+k >= W:
#                     flg = False
#                     break
#                 else:
#                     if S[i][j+k] == '#':
#                         flg = False
#                         break
#                     else:
#                         cnt += 1
#                 k += 1

#             ans = max(cnt, ans)

# # print(S)
# print(ans)
