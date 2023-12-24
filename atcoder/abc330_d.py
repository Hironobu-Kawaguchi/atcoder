# https://atcoder.jp/contests/abc330/tasks/abc330_d

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = [input() for _ in range(N)]

cnt_i, cnt_j = [0]*N, [0]*N
for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            cnt_i[i] += 1
            cnt_j[j] += 1

ans = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == 'x': continue
        ans += (cnt_i[i] - 1) * (cnt_j[j] - 1)
print(ans)
