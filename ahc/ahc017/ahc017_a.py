# https://atcoder.jp/contests/ahc017/tasks/ahc017_a

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
INF = 1001001001001
import math
import random
import time
import heapq
start = time.time()

# 入力
N, M, D, K = map(int, input().split())
G = [[] for _ in range(N)]
to = []
for i in range(M):
    u, v, w = map(int, input().split())
    u -= 1; v -= 1
    G[u].append((v, w, i))
    G[v].append((u, w, i))
    to.append((u, v, w))
# print(G)

# 1つの交差点から他の全交差点への距離合計（bfs）
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
        for nxt, w, idx in G[now]:
            if visited[nxt]: continue
            if under_construction!=None:
                if (now, nxt) in under_construction: continue
                if (nxt, now) in under_construction: continue
            heapq.heappush(hq, (d + w, nxt))
    ret = 0
    for i in range(N):
        ret += dist[i]
    # print(ret, dist)
    return ret

def calc_score(under_construction=None):
    ret = 0
    for i in range(N):
        ret += bfs(i, under_construction)
    # ret //= 2
    # print(ret, under_construction)
    return ret

base_score = calc_score(None)
# print(base_score)

def calc_all_score(under_construction=None):
    ret = 0
    for d in range(D):
        ret += calc_score(under_construction[d]) - base_score
    ret /= N * (N-1)
    ret = int(ret * 1000 / D * 10 + 5) // 10
    return ret

# 座標入力（省略可能）
# xy = []
# for i in range(N):
#     x, y = map(int, input().split())
#     xy.append((x, y, i))

# xy_link = []
# for i in range(M):
#     x = (xy[to[i][0]][0] + xy[to[i][1]][0]) // 2
#     y = (xy[to[i][0]][1] + xy[to[i][1]][1]) // 2
#     xy_link.append((x, y, i))
# xy_link.sort()
# print(xy_link)

# 初期解生成
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

# 工事日を入れ替えた時の不満度増減を計算
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

# 工事日を入れ替え処理
def swap_link(swap_idx):
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
    return

# print(score_change((1, 2)))
cnt = 0
while time.time() < start + 5.8:
    swap_idx = random.sample(range(K*D), 2)
    if swap_idx[0]>=M and swap_idx[1]>=M: continue
    if r[swap_idx[0]]==r[swap_idx[1]]: continue
    sc = score_change(swap_idx)
	# 焼きなまし法
    # NUM_LOOPS = 500
    # if cnt<NUM_LOOPS:
    #     T = 500000 - 450000 * (cnt / NUM_LOOPS)
    # else:
    #     T = 1.0
    # probability = math.exp(min((-sc) / T, 0))
    # # print(probability, T, swap_idx, sc)
    cnt += 1
    if sc<0:
    # if random.random() < probability:
        # 解が改善したときのみ P を更新する
        swap_link(swap_idx)
print(cnt)

# print(len(r[:M]))
print(*r[:M])
print(calc_all_score(uc_list))
