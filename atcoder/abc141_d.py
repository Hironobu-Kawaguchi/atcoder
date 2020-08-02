# https://atcoder.jp/contests/abc141/tasks/abc141_d

import heapq
N, M = map(int, input().split())
A = list(map(int, input().split()))

q = []
for i in range(N):
    heapq.heappush(q, -A[i])

for j in range(M):
    tmp = heapq.heappop(q)
    tmp = - (-tmp // 2)
    heapq.heappush(q, tmp)

ans = -sum(q)
print(ans)
