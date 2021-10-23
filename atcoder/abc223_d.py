# https://atcoder.jp/contests/abc223/tasks/abc223_d

import sys
input = sys.stdin.buffer.readline
import heapq

N, M = map(int, input().split())
to = [set() for _ in range(N+1)]
frm = [set() for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    to[A].add(B)
    frm[B].add(A)

q = []
for i in range(1, N+1):
    if len(frm[i])==0:
        heapq.heappush(q, i)

flag = True
pos = [-1] * (N+1)
cnt = 0
while q:
    now = heapq.heappop(q)
    cnt += 1
    pos[now] = cnt
    for v in to[now]:
        frm[v].remove(now)
        if len(frm[v])==0:
            heapq.heappush(q, v)
    to[now].clear()
# print(pos)
if cnt==N:
    ans = [-1] * N
    for i in range(1, N+1):
        ans[pos[i]-1] = i
    print(*ans)
else:
    print(-1)
