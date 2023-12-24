# https://atcoder.jp/contests/abc330/tasks/abc330_e

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

# https://qiita.com/Shirotsume/items/706742162db68c481c3c

from sortedcontainers import SortedSet

N, Q = map(int, input().split())
A = list(map(int, input().split()))

cnt = [0] * (N + 1)
for i in range(N):
    if A[i] > N: continue
    cnt[A[i]] += 1

SS = SortedSet()
for i in range(N + 1):
    if cnt[i] == 0:
        SS.add(i)

mex = SS[0]

# mex未満でcntが0のものができたら，それがmexになる
# xがmexの場合は，より上の値からmexになるものを探す
# 0 と N を繰り返すような場合はTLE
for k in range(Q):
    i, x = map(int, input().split())
    if A[i - 1] == x:   # 変更ない場合
        print(mex)
        continue
    if A[i - 1] <= N:
        cnt[A[i - 1]] -= 1
        if cnt[A[i - 1]] == 0:
            SS.add(A[i - 1])
    if x <= N:
        if cnt[x] == 0:
            SS.discard(x)
        cnt[x] += 1
    if A[i - 1] < mex and cnt[A[i - 1]] == 0:
        mex = A[i - 1]
    elif x == mex:
        mex = SS[0]
        # print(list(SS))
    A[i - 1] = x
    print(mex)
