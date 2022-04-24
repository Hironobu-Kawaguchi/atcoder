# https://atcoder.jp/contests/ahc010/tasks/ahc010_a

import sys
# input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
import time
start = time.time()

import random
import copy

vx = [-1, 0, 1, 0]
vy = [ 0,-1, 0, 1]
ROTATE = [1, 2, 3, 0, 5, 4, 7, 6]
TO = [
	[1, 0, -1, -1],
	[3, -1, -1, 0],
	[-1, -1, 3, 2],
	[-1, 2, 1, -1],
	[1, 0, 3, 2],
	[3, 2, 1, 0],
	[2, -1, 0, -1],
	[-1, 3, -1, 1],
    ]

N = 30
strT = [input() for _ in range(N)]
# T = [list(map(int, list(input()))) for _ in range(N)]
T = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        T[i][j] = int(strT[i][j])
print(T)

def calc_point(ans):
    print("calc_point", ans)
    point = 0
    rotateT = copy.copy(T)
    gone = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # rotateT[i][j] = int(T[i][j])
            print(i, j, ans[i*N+j], T[i][j])
            for _ in range(ans[i*N+j]):
                # print(i, j, int(rotateT[i][j]))
                rotateT[i][j] = ROTATE[int(rotateT[i][j])]
    # print(rotateT)

    def dfs(si, sj, v, i, j, L):
        if i==si and j==sj: return L+1
        nv = TO[rotateT[i][i]][(v+2)%4]
        ni, nj = i+vy[nv], j+vx[nv]
        if ni>=0 and ni<N and nj>=0 and nj<N and gone[ni][nj]==False and TO[rotateT[ni][ni]][(nv+2)%4]!=-1:
            L = dfs(i, j, v, ni, nj, 1)
        return -1

    Llist = []
    for i in range(N):
        for j in range(N):
            if gone[i][j]: continue
            print(i, j, rotateT[i][j])
            if rotateT[i][j] in [2, 3, 4, 5, 6]:
                nv = 2
                ni, nj = i+vy[nv], j+vx[nv]
                if ni>=0 and ni<N and nj>=0 and nj<N and gone[ni][nj]==False and TO[rotateT[ni][ni]][(nv+2)%4]!=-1:
                    L = dfs(i, j, nv, ni, nj, 1)
                    if L!=-1: Llist.append(L)
            if rotateT[i][j] in [5, 7]:
                nv = 3
                ni, nj = i+vy[nv], j+vx[nv]
                if ni>=0 and ni<N and nj>=0 and nj<N and gone[ni][nj]==False and TO[rotateT[ni][ni]][(nv+2)%4]!=-1:
                    L = dfs(i, j, nv, ni, nj, 1)
                    if L!=-1: Llist.append(L)
            if rotateT[i][j] not in [4, 5]:
                gone[i][j] = True

    point = 0
    if len(Llist)>=2:
        Llist.sort(reverse=True)
        point = Llist[0]*Llist[1]
    return point

best_ans = [0] * (N * N)
best_point = calc_point(best_ans)
# while time.time() < start + 1.8:
#     ans = random.choices(range(4), k=N*N)
#     point = calc_point(ans)
#     print(point, best_point, time.time() - start)
#     if point > best_point:
#         best_point = point
#         best_ans = copy.copy(ans)

# print(best_ans)
print(''.join(map(str, best_ans)))
