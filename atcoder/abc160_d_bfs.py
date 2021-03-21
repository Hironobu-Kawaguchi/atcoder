# https://atcoder.jp/contests/abc160/tasks/abc160_d
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

from collections import deque
INF = 1001001001
N, X, Y = map(int, input().split())
X -= 1; Y -= 1

ans = [0] * N
for sv in range(N):
    dist = [INF] * N
    q = deque()
    def push(v, d):
        if dist[v] != INF: return
        dist[v] = d
        q.append(v)
    push(sv, 0)
    while q:
        v = q.popleft()
        d = dist[v]
        if v-1 >= 0: push(v-1, d+1)
        if v+1 < N:  push(v+1, d+1)
        if v==X:     push(Y,   d+1)
        if v==Y:     push(X,   d+1)
    for i in range(N):
        ans[dist[i]] += 1

for i in range(1,N):
    print(ans[i]//2)
