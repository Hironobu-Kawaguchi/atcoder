# https://atcoder.jp/contests/abc015/tasks/abc015_3

import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for i in range(N)]
ans = 'Nothing'
for x in itertools.product(range(K), repeat=N):
    for i, j in enumerate(x):
        tmp = T[i][j]
        if i == 0:
            xor = tmp
        else:
            xor = xor ^ tmp
    if xor == 0:
        ans = "Found"
        break
print(ans)
