# https://atcoder.jp/contests/abc137/tasks/abc137_d

import heapq
N, M = map(int, input().split())

days = [[] for _ in range(M+1)]
for i in range(N):
    A, B = map(int, input().split())
    if A <= M:
        days[A].append(B)

ans = 0
q = []
for j in range(1, M+1):
    for k in days[j]:
        heapq.heappush(q, -k)

    if q:
        tmp = heapq.heappop(q)
        ans -= tmp
    
print(ans)
