# https://atcoder.jp/contests/abc271/tasks/abc272_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

from collections import deque

N, M = map(int, input().split())
move_list = []
x = 0
while x*x<=M:
    y = 0
    while y*y<=M-x*x:
        if x*x+y*y==M:
            move_list.append((x,y))
            break
        y += 1
    x += 1
# print(move_list)
ans = [[-1]*N for _ in range(N)]
q = deque([(0,0,0)])
while q:
    x, y, cnt = q.pop()
    # print(x, y, cnt)
    if ans[x][y]==-1:
        ans[x][y] = cnt
        for mx, my in move_list:
            if 0<=x+mx<N and 0<=y+my<N:
                q.appendleft((x+mx, y+my, cnt+1))
            if 0<=x-mx<N and 0<=y+my<N:
                q.appendleft((x-mx, y+my, cnt+1))
            if 0<=x+mx<N and 0<=y-my<N:
                q.appendleft((x+mx, y-my, cnt+1))
            if 0<=x-mx<N and 0<=y-my<N:
                q.appendleft((x-mx, y-my, cnt+1))
for i in range(N):
    print(*ans[i])
