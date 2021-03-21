# https://atcoder.jp/contests/abc149/tasks/abc149_e
# https://atcoder.jp/contests/abc149/submissions/9219994 # 写経

import sys
readline = sys.stdin.buffer.readline
import numpy as np
# 価値 x 以上になる握手の方法が M通りになる Xを二分探索で求める

N,M = map(int,readline().split())
A = np.array(readline().split(),np.int64)
A.sort()

def shake_cnt(x):
    # 価値 x 以上の握手を全て行うとして、前通りからx未満の回数を引く
    X = np.searchsorted(A,x-A)  # A の binary-serch を Aの値別に行った結果の配列
    return N * N - X.sum()

# 二分探索
left = 0        # 握手の回数がM以上の価値
right = 10 ** 6 # 握手の回数がM未満の価値
while left + 1 < right:
    x = (left + right) // 2
    if shake_cnt(x) >= M:
        left = x
    else:
        right = x

# 価値 right 以上の握手を全て行ったとして、回数と総和を計算
X = np.searchsorted(A,right-A) # 握手しない人数の左手別配列
Acum = np.zeros(N+1,np.int64)  # 価値 -> 累積和
Acum[1:] = np.cumsum(A)

shake = N * N - X.sum()     # 価値 right 以上の握手の回数
happy = (Acum[-1] - Acum[X]).sum() + (A * (N - X)).sum()    # 価値 right 以上の握手の価値の合計（左手＋右手）

happy += (M - shake) * left     # 価値 left の握手の価値を加算(M回までの制約なので、価値 left の全ての組み合わせとは限らない)
print(happy)


# TLE解法
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort(reverse=True)

# AA = []
# for i in range(N):
#     for j in range(N):
#         AA.append(A[i]+A[j])
# AA.sort(reverse=True)

# ans = 0
# for i in range(M):
#     ans += AA[i]

# print(ans)
