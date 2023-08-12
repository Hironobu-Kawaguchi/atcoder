# https://atcoder.jp/contests/abc314/tasks/abc314_d
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = list(input())
Q = int(input())
# print(S, file=sys.stderr)

lu_flg = 1  # 1:指定なし，2:小文字，3:大文字
special_char = dict()

for qi in range(Q):
    t, x, c = input().split()
    if t=="1":
        x = int(x) - 1
        S[x] = c
        special_char[x] = c
    elif t=="2":
        lu_flg = 2
        special_char = dict()
    elif t=="3":
        lu_flg = 3
        special_char = dict()

ans = []
for i in range(N):
    if lu_flg==1:
        ans.append(S[i])
    elif lu_flg==2:
        if i in special_char:
            ans.append(special_char[i])
        else:
            ans.append(S[i].lower())
    elif lu_flg==3:
        if i in special_char:
            ans.append(special_char[i])
        else:
            ans.append(S[i].upper())
print("".join(ans))
