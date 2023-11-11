# https://atcoder.jp/contests/arc162/tasks/arc162_c
# from numba import njit
# from functools import lru_cache


import sys

N = int(input())
P = list(map(int, (input().split())))

def double_swap(P, i, j):
    Q = P[:i] + P[i+2:]
    return Q[:j] + P[i:i+2] + Q[j:]

ans = []
for m in range(1, N-1):     # 1...N-2
    i = P.index(m)          # mの位置
    if i==m-1: continue     # 既にmが昇順に並んでいる場合はスキップ
    if i==N-1:              # mが末尾にある場合は一度1つ前に移動させる
        P = double_swap(P, i-1, i-2)
        ans.append((i-1+1, i-2))
        i -= 1
        # print(*ans[-1], P, file=sys.stderr)
    j = m-1                 # mの移動先をしている1つ前にjを設定
    P = double_swap(P, i, j)
    ans.append((i+1, j))
    # print(*ans[-1], P, file=sys.stderr)
if P[-2]>P[-1]:     # 最後の2つが逆順になっている場合は、不可能
    print("No")
else:
    print("Yes")
    print(len(ans))
    for i, j in ans:
        print(i, j)


# import sys
# input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# # sys.setrecursionlimit(10 ** 7)


# N = int(input())
# P = list(map(int, (input().split())))
# # print(P)

# def pos(P):
#     res = [-1] * N
#     for i in range(N):
#         res[P[i]-1] = i
#     return res
# pos_list = pos(P)
# # print(pos_list)

# delete_flg = [True] * N
# delete_cnt = 0

# ans = []
# now = N
# while True:
#     if len(P)-delete_cnt<=2:
#         break
#     if now==P[-1]:
#         now -= 1
#         P.pop()
#         continue
#     i = pos_list[now-1] - 1
#     if i==-1:
#         i = 0
#     j = now - 2
#     ans.append((i+1-delete_cnt, j))
#     # print(now, ans[-1][0], ans[-1][1])
#     P.append(P[i])
#     P.append(P[i+1])
#     pos_list[P[i]-1] = len(P) - 2
#     pos_list[P[i+1]-1] = len(P) - 1
#     delete_flg[i] = False
#     delete_flg[i+1] = False
#     delete_cnt += 2
#     # print(P)
#     # print(delete_flg)


# if len(P)!=delete_cnt and P[-2]>P[-1]:
#     print("No")
# else:
#     print("Yes")
#     print(len(ans))
#     for i, j in ans:
#         print(i, j)


