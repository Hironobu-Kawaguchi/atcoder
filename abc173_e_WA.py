# https://atcoder.jp/contests/abc173/tasks/abc173_e

import sys
input = sys.stdin.buffer.readline
MOD = 10**9 + 7
N, K = map(int, input().split())
A = list(map(int, (input().split())))
ap = []
neg_cnt = 0
pos_cnt = 0
zero_cnt = 0
for a in A:
    if a<0:
        ap.append((-a, 1))     # sortで先に来るようマイナスを1にする
        neg_cnt += 1
    elif a==0:
        ap.append((0, 0))
        zero_cnt += 1
    else:
        ap.append((a, -1))
        pos_cnt += 1
ap.sort(reverse=True)
# print(ap)
ans = 1
if neg_cnt==N and K%2:      # 全てが負で奇数個選ぶので、答えは負
    for i in range(K):
        ans *= ap[N-i-1][0] * ap[N-i-1][1] * -1
        ans %= MOD
else:                       # 答えは正
    neg_num = 0
    pos_num = 0
    for i in range(K):
        if ap[i][1] == 1:
            neg_num += 1
        elif ap[i][1] == -1:
            pos_num += 1
    if neg_num % 2:     # 負の数が奇数だったら、-1して偶数回にし、正が出るまで見る
        if pos_num == pos_cnt:
            pos_flg = True
            neg_num += 1    # もう正がない
        else:
            neg_num -= 1
    i = 0
    cnt = 0
    while cnt < K and i < N:
    # for i in range(K):
        if ap[i][1] == 1:  # 負の数だったら、neg_num回まで
            if neg_num == 0:
                i += 1
                continue
            else:
                neg_num -= 1
        if ap[i][1] == -1: 
            if pos_num == 0:
                i += 1
                continue
            else:
                pos_num -= 1
        ans *= ap[i][0] * ap[i][1] * -1
        ans %= MOD
        cnt += 1
        i += 1

print(ans)
