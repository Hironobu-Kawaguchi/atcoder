# https://atcoder.jp/contests/past201912/tasks/past201912_e

import copy
N ,Q = map(int, input().split())
f = [[0]* N for _ in range(N)]

for q in range(Q):
    S = list(map(int, input().split()))
    if S[0] == 1:
        f[S[1]-1][S[2]-1] = 1
    elif S[0] == 2:
        for i in range(N):
            if f[i][S[1]-1] == 1:
                f[S[1]-1][i] = 1
    else:
        # print(f)
        tmp = copy.copy(f[S[1]-1])
        for j in range(N):
            if tmp[j] == 1:
                # print(f[S[1]-1][j], S[1]-1, j, f[0])
                for k in range(N):
                    if f[j][k] == 1 and S[1]-1 != k:
                        f[S[1]-1][k] = 1
            else:
                continue
        # print(f)

# print(f)
for i in range(N):
    ans = ''
    for j in range(N):
        if f[i][j]:
            ans += 'Y'
        else:
            ans += 'N'
    print(ans)
