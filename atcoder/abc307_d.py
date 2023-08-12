# https://atcoder.jp/contests/abc307/tasks/abc307_d
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input()

q = []
qq = []
for i in range(N):
    if S[i]=='(':
        q.append(S[i])
        qq.append(S[i])
    elif S[i]==')':
        if not qq or (qq and qq[-1]!='('):   # ()の最後が(でない場合，)は消せない
            q.append(S[i])
            qq.append(S[i])
            continue
        while q:    # 消せる場合
            if q[-1]=='(':  # (まで行ったら消して終わる
                q.pop()
                qq.pop()
                break
            else:   # 英小文字の場合消す
                q.pop()
    else:
        q.append((S[i]))
    # print(i, q)
print("".join(q))
