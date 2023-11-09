# https://atcoder.jp/contests/arc166/tasks/arc166_a
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

def main():
    N, X, Y = input().split()
    cnt = [0] * 3
    for x, y in zip(X, Y):
        cnt["ABC".index(x)] += 1   # Xの残り文字を数える
        if y=='A':                      # YがAなら，Xに先にBが出てなければOK
            if cnt[0]: cnt[0] -= 1      # XにAがあれば消す
            elif cnt[2]: cnt[2] -= 1    # XにAがなければCを消す
            else:                       # XにAもCもなければ，BなのでNo
                print('No')
                return
        elif y=='B':                    # YがBなら
            cnt[1] -= 1                 # XのBの数を引く（マイナスもあり）
        elif y=='C':                    # YがCなら
            if x!=y:                    # XもCでなければNo
                print('No')
                return
            if cnt[0]:                  # Aが残っていたら，AとBの数が合わないのでダメ
                print('No')
                return
            cnt[1] = cnt[2] = 0         # Aがなければ，BとCの数を0にリセットする
    if cnt[0]:                          # 最後，Aが残っていたらダメ
        print('No')
        return
    print('Yes')
    return

T = int(input())
for ti in range(T):
    main()



# TLE
# def check(x, y):
#     cnt_A = y.count('A') - x.count('A')
#     cnt_B = y.count('B') - x.count('B')
#     if cnt_A<0 or cnt_B<0:
#         return False
#     x_change = ''
#     for i in range(len(x)):
#         if x[i]=='C':
#             if cnt_A>0:
#                 x_change += 'A'
#                 cnt_A -= 1
#             else:
#                 x_change += 'B'
#                 cnt_B -= 1
#         else:
#             x_change += x[i]
#     x_a_idxs, y_a_idxs = [], []
#     for i in range(len(x_change)):
#         if x_change[i]=='A':
#             x_a_idxs.append(i)
#         if y[i]=='A':
#             y_a_idxs.append(i)
#     for i, j in zip(x_a_idxs, y_a_idxs):
#         if i>j:
#             return False
#     return True

# def main():
#     N, X, Y = input().split()
#     Xs, Ys = [], []
#     x, y = '', ''
#     for i in range(len(Y)):
#         if Y[i]=='C':
#             if X[i]!="C":
#                 print('No')
#                 return
#             Xs.append(x)
#             Ys.append(y)
#             x, y = '', ''
#         else:
#             x += X[i]
#             y += Y[i]
#     Xs.append(x)
#     Ys.append(y)
#     for x, y in zip(Xs, Ys):
#         if not check(x, y):
#             print('No')
#             return
#     print('Yes')
#     return

# T = int(input())
# for ti in range(T):
#     main()




# from collections import Counter

# def main():
#     N, X, Y = input().split()
#     N = int(N)
#     idx_cut = [0]
#     for i in range(N-1):
#         # if (Y[i]=='B' or Y[i]=='A') and Y[i+1]=='A':
#         #     continue
#         # elif Y[i]=='B' and Y[i+1]=='B':
#         #     continue
#         # else:
#         #     idx_cut.append(i+1)
#         if Y[i:i+2]=='AB' or Y[i]=='C' or Y[i+1]=='C':
#             idx_cut.append(i+1)
#     idx_cut.append(N)
#     # print(*idx_cut, file=sys.stderr)
#     for i in range(len(idx_cut)-1):
#         x = X[idx_cut[i]:idx_cut[i+1]]
#         y = Y[idx_cut[i]:idx_cut[i+1]]
#         print(X, Y, idx_cut[i], idx_cut[i+1], x, y, file=sys.stderr)
#         x_cnt = Counter(x)
#         y_cnt = Counter(y)
#         if x_cnt['A']>y_cnt['A'] or x_cnt['B']>y_cnt['B'] or x_cnt['C']<y_cnt['C']:
#         # if x_cnt['A']>y_cnt['A'] or x_cnt['B']>y_cnt['B']:
#             print('No')
#             return
#         # idx_B, idx_A = N, 0
#         # for j in range(len(x)):
#         #     if x[j]=='A':
#         #         idx_A = max(idx_A, j)
#         #     elif x[j]=='B':
#         #         idx_B = min(idx_B, j)
#         # if idx_B<idx_A:
#         #     print('No')
#         #     return
#     print('Yes')
#     return

# T = int(input())
# for ti in range(T):
#     main()
