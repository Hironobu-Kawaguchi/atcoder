# https://atcoder.jp/contests/abc167/tasks/abc167_f

import sys
def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
tbl = []
sum_left, sum_right, sum_maxdif, sum_dif = 0, 0, 0, 0
for i in range(N):
    S = input()
    left = 0
    right = 0
    maxdif = 0
    for c in S:
        if c=='(':
            left += 1
        else:
            right += 1
        maxdif = max(maxdif, right - left)
    if S[0] == '(':
        s = True
    else:
        s = False
    if S[-1] == ')':
        e = True
    else:
        e = False
    tbl.append([left-right, left, right, maxdif, s, e])
    sum_left += left
    sum_right += right
    sum_maxdif += maxdif
    sum_dif += max(left-right, 0)
tbl.sort()
for i in range(N):
    if tbl[i][5]:
        if tbl[i][0] > 0:
            sum_dif -= tbl[i][0]
        break
for i in range(N-1, -1, -1):
    if tbl[i][4]:
        if tbl[i][3] < 0:
            sum_dif -= tbl[i][0]
        break
    
if sum_left != sum_right:
    print('No')
elif sum_maxdif > sum_dif:
    print('No')
else:
    print('Yes')


# N = int(input())
# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
