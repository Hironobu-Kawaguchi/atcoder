# https://atcoder.jp/contests/zone2021/tasks/zone2021_e

from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix
R, C = map(int, input().split())
data = []
row = []
column = []
for i in range(R):
    a = list(map(int, input().split()))
    for j in range(C - 1):
        x = i * C + j
        y = i * C + j + 1
        row += [x, y]
        column += [y, x]
        data += [a[j], a[j]]
for i in range(R - 1):
    a = list(map(int, input().split()))
    for j in range(C):
        x = i * C + j
        y = i * C + j + C
        row += [x, y + R * C]
        column += [y, x + R * C]
        data += [a[j], 1]
for i in range(R):
    for j in range(C):
        x = i * C + j
        y = x + R * C
        row += [x, y]
        column += [y, x]
        data += [1, 0]
# print(data)
g = csr_matrix((data, (row, column)))
print(int(shortest_path(g, indices=0)[R * C - 1]))

# TLE
# import heapq
# INF = 1001001001

# R, C = map(int, input().split())
# A = [[int(i) for i in input().split()] for _ in range(R)]
# B = [[int(i) for i in input().split()] for _ in range(R-1)]
# # print(R, C)
# # print(A)
# # print(B)

# dist = [[[INF]*2 for _ in range(C)] for _ in range(R)]
# # print(dist)

# q = [(0,0,0,0)]
# while len(q)>0:
#     cost, r, c, f = heapq.heappop(q)
#     # print(cost, r, c, f)
#     if dist[r][c][f] <= cost: continue
#     dist[r][c][f] = cost
#     if r==R-1 and c==C-1 and f==0:
#         ans = cost
#         break
#     if f==0:
#         if c<C-1: heapq.heappush(q, (cost+A[r][c], r, c+1, f))
#         if c>0:   heapq.heappush(q, (cost+A[r][c-1], r, c-1, f))
#         if r<R-1: heapq.heappush(q, (cost+B[r][c], r+1, c, f))
#         heapq.heappush(q, (cost+1, r, c, 1))
#     else:
#         if r>0: heapq.heappush(q, (cost+1, r-1, c, f))
#         heapq.heappush(q, (cost, r, c, 0))

# print(ans)
