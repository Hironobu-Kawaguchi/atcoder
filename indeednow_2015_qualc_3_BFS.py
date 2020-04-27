# https://atcoder.jp/contests/indeednow-qualb/tasks/indeednow_2015_qualc_3

import heapq

N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
# print(G)

q = []
heapq.heappush(q, 0)
done = [0] * N
ans = []
while q:
    now = heapq.heappop(q)
    ans.append(now+1)
    done[now] = 1
    for nxt in G[now]:
        if done[nxt]: continue
        heapq.heappush(q, nxt)
print(*ans)
