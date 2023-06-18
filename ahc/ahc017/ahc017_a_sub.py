# https://atcoder.jp/contests/ahc017/tasks/ahc017_a

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
INF = 1001001001001
import random
import time
import heapq
start = time.time()

N, M, D, K = map(int, input().split())
G = [[] for _ in range(N)]
to = []
for i in range(M):
    u, v, w = map(int, input().split())
    u -= 1; v -= 1
    G[u].append((v, w))
    G[v].append((u, w))
    to.append((u, v, w, i))
# print(G)

xy = []
for i in range(N):
    x, y = map(int, input().split())
    xy.append((x, y, i))

# xy_link = []
# for i in range(M):
#     x = min(xy[to[i][0]][0], xy[to[i][1]][0])
#     y = min(xy[to[i][0]][1], xy[to[i][1]][1])
#     xy_link.append((x, y, i))
# xy_link.sort()
# print(xy_link)

uc_list = [set() for _ in range(D)]
r = []
for i in range(K*D):
    r.append(i%D + 1)
    if i<M:
        uc_list[i%D].add((to[i][0], to[i][1]))
    #     r.append(xy_link[i][2]%D + 1)
    # else:
    #     r.append(i%D + 1)
# print(len(r), r)
# print(uc_list)


def bfs(start=0, under_construction=None):
    visited = [False] * N
    dist = [10**9] * N
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        d, now = heapq.heappop(hq)
        if visited[now]: continue
        dist[now] = d
        visited[now] = True
        for nxt, w in G[now]:
            if visited[nxt]: continue
            if (now, nxt) in under_construction: continue
            if (nxt, now) in under_construction: continue
            heapq.heappush(hq, (d + w, nxt))
    ret = 0
    for i in range(N):
        ret += dist[i]
    # print(ret, dist)
    return ret

def score_change(swap_idx):
    swap_set, swap_day = [], []
    for i in range(2):
        swap_day.append(r[swap_idx[i]])
        if swap_idx[i]<M:
            swap_set.append(set([(to[swap_idx[i]][0], to[swap_idx[i]][1])]))
        else:
            swap_set.append(set())
    ret = 0
    node_list = []
    for i in range(2):
        if len(swap_set[i])==0: continue
        for tpl in swap_set[i]:
            for j in range(2):
                node_list.append(tpl[j])
    node_list = list(set(node_list))
    # print(node_list)
    for i in node_list:
    # for i in range(N):
    # for i in random.sample(range(N), 20):
        for j in range(2):
            # print(swap_set[j], swap_set[1-j])
            ret += bfs(i, uc_list[swap_day[j]-1] - swap_set[j] | swap_set[1-j])
            ret -= bfs(i, uc_list[swap_day[j]-1])
            # print(ret)
    return ret

# print(score_change((1, 2)))
# cnt = 0
while time.time() < start + 5.9:
    # cnt += 1
    swap_idx = random.sample(range(K*D), 2)
    if swap_idx[0]>=M and swap_idx[1]>=M: continue
    if r[swap_idx[0]]==r[swap_idx[1]]: continue
    sc = score_change(swap_idx)
    if sc<0:
        if swap_idx[0]<M:
            st0 = set([(to[swap_idx[0]][0], to[swap_idx[0]][1])])
        else:
            st0 = set()
        if swap_idx[1]<M:
            st1 = set([(to[swap_idx[1]][0], to[swap_idx[1]][1])])
        else:
            st1 = set()
        uc_list[r[swap_idx[0]]-1] -= st0
        uc_list[r[swap_idx[0]]-1] |= st1
        uc_list[r[swap_idx[1]]-1] -= st1
        uc_list[r[swap_idx[1]]-1] |= st0
        r[swap_idx[0]], r[swap_idx[1]] = r[swap_idx[1]], r[swap_idx[0]]
        # print(swap_idx, sc)
# print(cnt)

# print(len(r[:M]))
print(*r[:M])
