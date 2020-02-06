# https://atcoder.jp/contests/arc041/tasks/arc041_b

N, M = map(int, input().split())
b = [list(map(int, list(input()))) for _ in range(N)]
# print(b)
a = [[0] * M]
for i in range(N-1):
    a.append(b[i])
    for j in range(M):
        if b[i][j] != 0:
            b[i+1][j-1] -= b[i][j]
            b[i+1][j+1] -= b[i][j]
            b[i+2][j]   -= b[i][j]
for i in range(N):
    print(''.join(map(str, a[i])))
