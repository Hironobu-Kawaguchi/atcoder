# https://atcoder.jp/contests/past201912/tasks/past201912_g
# 3つ以下のグループ -> 2or3 1だったら幸福度0

from itertools import product, combinations

N = int(input())
A = [[0] * N for _ in range(N)]
for i in range(N-1):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        A[i][i+j+1] = a[j]
        A[i+j+1][i] = a[j]
# print(A)

ans = -1000000000
for p in product([0, 1, 2], repeat=N-1):
    # print(p)
    s = [[0], [], []]
    for i in range(N-1):
        s[p[i]].append(i+1)
    # print(s)
    tmp = 0
    for i in range(3):
        for c in combinations(s[i], 2):
            tmp += A[c[0]][c[1]]
            # print(c)
    ans = max(ans, tmp)
    # print(p, s, tmp)

print(ans)
