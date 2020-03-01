# https://atcoder.jp/contests/abc157/tasks/abc157_b

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

A = [list(map(int, (input().split()))) for _ in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]

chk = [[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        if A[i][j] in b:
            chk[i][j] = 1

ans = "No"
for i in range(3):
    if chk[i][0] == chk[i][1] == chk[i][2] == 1:
        ans = "Yes"
        break
    if chk[0][i] == chk[1][i] == chk[2][i] == 1:
        ans = "Yes"
        break
if chk[0][0] == chk[1][1] == chk[2][2] == 1:
    ans = "Yes"
elif chk[0][2] == chk[1][1] == chk[2][0] == 1:
    ans = "Yes"

print(ans)
