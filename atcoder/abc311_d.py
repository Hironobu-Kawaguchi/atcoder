# https://atcoder.jp/contests/abc310/tasks/abc310_d
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
S = [input() for _ in range(N)]

xi = [0, 1, 0, -1]
yi = [1, 0, -1, 0]

from collections import deque
q = deque()
q.append((1, 1, 0))
q.append((1, 1, 1))
st = set()
st.add((1, 1, 0))
st.add((1, 1, 1))
visited = [[False]*M for _ in range(N)]
visited[1][1] = True
while q:
    x, y, d = q.popleft()
    while True:
        if S[y+yi[d]][x+xi[d]]=='#':
            break
        x += xi[d]
        y += yi[d]
        visited[y][x] = True
    for d in range(4):
        if S[y+yi[d]][x+xi[d]]=='#': continue
        if (x, y, d) not in st:
            q.append((x, y, d))
            st.add((x, y, d))
ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            ans += 1
print(ans)
