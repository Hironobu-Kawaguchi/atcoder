# https://atcoder.jp/contests/abc325/tasks/abc325_c

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
S = [input() for _ in range(H)]

gone = [[False]*W for _ in range(H)]
ans = 0

# BFS
from collections import deque
q = deque()
for i in range(H):
    for j in range(W):
        if S[i][j] != "#": continue
        if gone[i][j]: continue
        ans += 1
        q.append((i, j))
        while len(q):
            x, y = q.popleft()
            if gone[x][y]: continue
            gone[x][y] = True
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0: continue
                    if 0<=x+dx<H and 0<=y+dy<W and S[x+dx][y+dy]=="#":
                        q.append((x+dx, y+dy))
print(ans)
