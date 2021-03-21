# https://atcoder.jp/contests/abc157/tasks/abc157_a
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

A = [[int(i) for i in input().split()] for _ in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]
# print(A)
# print(b)

done = [[0] * 3 for _ in range(3)]
for k in range(N):
    for i in range(3):
        for j in range(3):
            if b[k] == A[i][j]:
                done[i][j] = 1
# print(done)

ans = "No"
for i in range(3):
    flg = True
    for j in range(3):
        if done[i][j] == 0:
            flg = False
    if flg:
        ans = "Yes"
for i in range(3):
    flg = True
    for j in range(3):
        if done[j][i] == 0:
            flg = False
    if flg:
        ans = "Yes"

flg = True
for j in range(3):
    if done[j][j] == 0:
        flg = False
if flg:
    ans = "Yes"
flg = True
for j in range(3):
    if done[2-j][j] == 0:
        flg = False
if flg:
    ans = "Yes"

print(ans)


# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
