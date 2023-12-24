# https://atcoder.jp/contests/ahc027/tasks/ahc027_a
import sys
from collections import deque
from itertools import permutations
import heapq
sys.setrecursionlimit(1000000)
import math
import numpy as np
import random
import time

# 時間を計測
start_time = time.time()
LIMIT_TIME = 1.0

# 入力
N = int(input())
h = [input() for _ in range(N-1)]
v = [input() for _ in range(N)]
d = [list(map(int, input().split())) for _ in range(N)]
sum_dust = sum([sum(d[i]) for i in range(N)])

# 移動の管理
visited = [False for _ in range(N*N)]
visited[0] = True
visited_count = 1
DIJ = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIR = "RDLU"

def ij2k(i, j):
    return i * N + j

def k2ij(k):
    return k // N, k % N

def d_k(k):
    return d[k // N][k % N]

# Graphにする　k = i * N + j
G = [[] for _ in range(N * N)]
for i in range(N):
    for j in range(N):
        k = i * N + j
        if i < N - 1:
            if h[i][j] == '0':
                k2 = (i + 1) * N + j
                G[k].append((k2, d[i+1][j], 1))  # D
                G[k2].append((k, d[i][j], 3))    # U
        if j < N - 1:
            if v[i][j] == '0':
                k2 = i * N + j + 1
                G[k].append((k2, d[i][j+1], 0))  # R
                G[k2].append((k, d[i][j], 2))    # L

# DFS
def dfs(k):
    global visited_count
    # print("visited count", visited_count, k, file=sys.stderr)
    if visited_count >= N * N: return
    if not visited[k]: visited_count += 1
    visited[k] = True
    dirs = []
    for k2, dust, dir in G[k]:
        if not visited[k2]:
            # dirs.append((-dust, len(G[k2]), k2, dir))
            dirs.append((len(G[k2]), k2, dir))
    dirs.sort()
    # for _, _, k2, dir in dirs:
    for _, k2, dir in dirs:
        if not visited[k2]:
            ans.append(k2)  # 往路
            dfs(k2)
            if visited_count < N * N:
                ans.append(k)   # 復路
    return ans

# BFSで2点間の最短距離を求める
def bfs_dist(start, goal):
    # print("start bfs", start, goal, file=sys.stderr)
    if dist_kk[start][goal] != -1: return dist_kk[start][goal]  # memo化
    dist = [-1 for _ in range(N*N)]
    q = deque([(start, 0)])
    while q:
        k, _d = q.popleft()
        if dist[k] != -1: continue
        dist[k] = _d
        dist_kk[start][k] = _d
        if k == goal: break
        for k2, dust, _ in G[k]:
            if dist[k2] == -1:  # 未訪問
                q.append((k2, _d + 1))
    return dist[goal]

# BFSで開始点からの全ての点への最短距離を求める
def bfs_all_dist(start):
    # print("start bfs", start, file=sys.stderr)
    dist = [-1 for _ in range(N*N)]
    q = deque([(start, 0)])
    while q:
        k, _d = q.popleft()
        if dist[k] != -1: continue
        dist[k] = _d
        for k2, dust, _ in G[k]:
            if dist[k2] == -1:  # 未訪問
                q.append((k2, _d + 1))
    return dist

# BFSで最短経路を求める goalは含むが，startは含まない
def bfs(start, goal, update_visited=False):
    if update_visited:
        global visited_count
    print("start bfs", start, goal, file=sys.stderr)
    dist = [-1 for _ in range(N*N)]
    q = deque([(start, 0)])
    while q:
        k, _d = q.popleft()
        if dist[k] != -1: continue
        dist[k] = _d
        if k == goal: break
        for k2, dust, _ in G[k]:
            if dist[k2] == -1:  # 未訪問
                q.append((k2, _d + 1))
    print("start route search", start, goal, file=sys.stderr)
    route = []
    now = goal
    while now != start:
        route.append(now)
        if update_visited: 
            if not visited[now]: visited_count += 1
            visited[now] = True
        for k2, dust, dir in G[now]:
            if dist[k2] == dist[now] - 1:
                now = k2
                break
    return route[::-1]

# dijkstraで最短経路でdustが高い経路を求める goalは含むが，startは含まない
def dijkstra(start, goal, update_visited=False):
    if update_visited:
        global visited_count
    weight = 10**5    # weight - dustをエッジの重みとする．dust <= 10**3なので余裕を見た数字．
    # print("start dijkstra", start, goal, file=sys.stderr)
    dist = [-1 for _ in range(N*N)]
    q = [(0, start)]
    while q:
        _d, k = heapq.heappop(q)
        if dist[k] != -1: continue
        dist[k] = _d
        if k == goal: break
        for k2, dust, _ in G[k]:
            if dist[k2] == -1:  # 未訪問
                heapq.heappush(q, (_d + weight - dust, k2))
    # print("start route search", start, goal, file=sys.stderr)
    route = []
    now = goal
    while now != start:
        route.append(now)
        if update_visited: 
            if not visited[now]: visited_count += 1
            visited[now] = True
        # 優先するルートを選ぶ まだ訪問していない点の中で最もdustが高い点を選ぶ
        cand_route = []
        for k2, dust, dir in G[now]:
            if dist[k2] == -1: continue # 最短ルートではないルート
            if dist[k2] >= dist[now]: continue # 最短ルートではないルート
            cand_route.append((-visited[k2], dust, k2, dir))
        cand_route.sort(reverse=True)
        now = cand_route[0][2]
        # for _, _, k2, _ in cand_route:
        #     # if dist[k2] == -1: continue
        #     if dist[k2] < dist[now]:
        #         now = k2
        #         break
    return route[::-1]

# 重複する移動を削除
def remove_dup(ans):
    start_len = len(ans)
    # 累積和で区間の到達回数を管理
    cum = [[0 for _ in range(N * N)] for _ in range(len(ans) + 1)]
    for i in range(len(ans)):
        for j in range(N * N):
            cum[i+1][j] = cum[i][j]
        cum[i+1][ans[i]] += 1
    now = len(ans) - 1
    while now > 0:
        for pre in range(now - 1, -1, -1):
            if cum[pre][ans[pre]] == 0:  # preより前に到達していないので消せない
                break
        if pre + 1 == now:  # 消せない
            now -= 1
            continue
        # print("remove dup check", now, pre, file=sys.stderr)
        route = dijkstra(ans[pre + 1], ans[now])
        # print("remove dup route", now, pre+1, now - pre -2, len(route)-1, file=sys.stderr)
        ans = ans[:pre + 2] + route[:-1] + ans[now:]
        now = pre + 1
        # for i in range(pre + 1, now):
        #     if ans[i] in G[ans[now]]:   # ans[i]とans[now]がつながっている
        #         print("remove dup check", now, i, file=sys.stderr)
        #         ans = ans[:i+1] + ans[now:]
        #         now = i
        #         break
        # else:
        #     now -= 1
        # if cum[now][ans[now]] > 1:  # nowより前に既に到達している
        #     pre = now - 1
        #     while pre > 0 and ans[pre] != ans[now]: # 前回到達した時
        #         pre -= 1
        #     # print("remove dup check", now, pre, file=sys.stderr)
        #     ok = True
        #     for k in range(N * N):  # pre と now の間に到達したすべての場所をその前に既に到達しているか確認
        #         if cum[now][k] - cum[pre + 1][k] > 0:
        #             if cum[pre][k] == 0:    # 到達していない
        #                 ok = False
        #                 break
        #     if ok:
        #         print("remove dup", now, pre, file=sys.stderr)
        #         ans = ans[:pre] + ans[now:]
        #         now = pre
        #     else:
        #         now -= 1
        # else:
        #     now -= 1
    print("remove dup end", start_len, "->", len(ans), file=sys.stderr)
    return ans

# 移動の推移から回答を出力
def print_ans(ans):
    for i in range(len(ans) - 1):
        k = ans[i]
        k2 = ans[i+1]
        if k2 == k: continue
        if k2 - k == 1:
            print("R", end='')
        elif k2 - k == -1:
            print("L", end='')
        elif k2 - k == N:
            print("D", end='')
        elif k2 - k == -N:
            print("U", end='')
        else:
            print("Error can not move (not neighborhood)", k, "->", k2, file=sys.stderr)
    print()

def calc_dust(ans): ### ansの後の各点の汚れを計算し，(dust, k)のリストを降順で返す
    _L = len(ans) - 1
    _last_visit = [-1 for _ in range(N * N)]
    _visit_count = 0
    for i in range(_L, -1, -1):
        if _last_visit[ans[i]] == -1:
            _visit_count += 1
            _last_visit[ans[i]] = i
        if _visit_count == N * N:
            break
    _dust = []
    for k in range(N * N):
        _dust.append((d_k(k) * (_L - _last_visit[k]), k))
    _dust.sort(reverse=True)
    return _dust

def calc_score(ans):
    L = len(ans) - 1
    # 1巡目
    last_visit = [-1 for _ in range(N * N)]
    for i in range(L):
        k = ans[i + 1]
        last_visit[k] = i
    St = 0
    for i in range(N * N):
        try:
            St += d[i//N][i%N] * (L - 1 - last_visit[i])
        except:
            print("Error", d, i, N, L, file=sys.stderr)
    if -1 in last_visit:
        print("Error not all visit", file=sys.stderr)
        return 10**18
    # 2巡目
    score = 0
    for i in range(L):
        k = ans[i + 1]
        clean_dust = d[k//N][k%N] * (i + L - last_visit[k])
        last_visit[k] = i + L
        St += sum_dust - clean_dust
        score += St
    return score // L

def get_cut_index(k):
    i, j = k2ij(k)
    ii = i // cut_i
    jj = j // cut_j
    return ii * cut_num + jj

# 巡回セールスマン問題（Traveling Salesman Problem, TSP）を全探索で解く
def tsp(start, goal, node_list):    # 出力はハブのidxのリスト 1-indexed
    """
    start: 始点
    goal: 終点
    node_list: ノードのリスト
    """
    # ハブ間の最短距離を求める
    _node_list = [start] + node_list + [goal]
    dist_matrix = [[0 for _ in range(len(_node_list))] for _ in range(len(_node_list))]
    for i in range(len(_node_list)):
        for j in range(i + 1, len(_node_list)):
            dist_matrix[i][j] = dist_matrix[j][i] = bfs_dist(_node_list[i], _node_list[j])
    # print("hub_dist", *hub_dist, file=sys.stderr)
    min_score = 10**18
    min_ans = []
    for route in permutations(range(1, len(_node_list) - 1)):
        # print("tsp route", start, *route, goal, file=sys.stderr)
        score = dist_matrix[0][route[0]]    # 始点から最初のノードへの距離
        for i in range(len(route) - 1):
            score += dist_matrix[route[i]][route[i+1]]  # ノード間の距離
        score += dist_matrix[route[-1]][len(_node_list)-1]   # 最後のノードから終点への距離
        if score < min_score:
            min_score = score
            min_ans = route
            # print("tsp score", min_score, *min_ans, file=sys.stderr)
    return list(min_ans)

# 1周するルートを求める
def route_cycle(ans, route, start=-1, goal=-1, update_visited=True):
    """
    ans: 現在の移動の推移
    route: 巡回するルート
    start: 始点がルートに含まれていない場合の始点
    goal: 終点がルートに含まれていない場合の終点
    """
    if start != -1:
        ans.extend(dijkstra(start, route[0], update_visited=update_visited))
    for i in range(len(route)-1):
        ans.extend(dijkstra(route[i], route[i+1], update_visited=update_visited))
    if goal != -1:
        ans.extend(dijkstra(route[-1], goal, update_visited=update_visited))
    # else:
    #     ans.extend(dijkstra(route[-1], route[0], update_visited=update_visited))  # goalがない場合は始点に戻る
    return ans


# # 次数が2以下，汚れやすさ上位10%の点をハブとして選ぶ ただし1本道は除く
# def create_hub_list():
#     hub_set = set()
#     dust_list = []
#     for k in range(N * N):
#         if len(G[k]) == 1 or (len(G[k]) == 2 and abs(G[k][0][0] - k) != abs(G[k][1][0] - k)):
#             hub_set.add(k)
#         dust_list.append((d_k(k), k))
#     dust_list.sort(reverse=True)
#     for _, k in dust_list[:N * N // 10]:
#         hub_set.add(k)
#     hub_set.discard(0)  # 始点はハブにしない
#     return sorted(list(hub_set))

# 汚れやすさ上位20%の点をハブとして選ぶ
def create_hub_list():
    hub_set = set()
    dust_list = []
    for k in range(N * N):
        # if len(G[k]) == 1 or (len(G[k]) == 2 and abs(G[k][0][0] - k) != abs(G[k][1][0] - k)):
        #     hub_set.add(k)
        dust_list.append((d_k(k), k))
    dust_list.sort(reverse=True)
    # for _, k in dust_list[:N * N // 10]:
    for _, k in dust_list[:N * N // 5]:
        hub_set.add(k)
    # hub_set.discard(0)  # 始点はハブにしない
    return sorted(list(hub_set))

# 合計距離を計算する関数
def get_dist(P):
	ret = 0
	for i in range(len(P) - 1):
		ret += dist_kk[P[i]][P[i+1]]
	return ret

# 焼きなまし法によって最短ルートを求める関数
def simulated_annealing(points, start=0, goal=0):
	# 初期解生成
    P = []
    if start != -1: P.append(start)
    P.extend(points.copy())
    if goal != -1: P.append(goal)
    n = len(P) - 1
    current_score = get_dist(P)
    original_score = current_score
    # 焼きなまし法
    num_loops = 0
    # NUM_LOOPS = 150000
    NUM_LOOPS = 600000
    # for t in range(NUM_LOOPS):
    t = 0
    while time.time() - start_time < LIMIT_TIME:
        # 反転させる区間 [L, R] を選ぶ
        l = random.randint(1, n - 1) # 1 以上 n-1 以下のランダムな整数
        r = random.randint(1, n - 1) # 1 以上 n-1 以下のランダムな整数
        if l > r:
            l, r = r, l
        # P[l], P[l+1], ..., P[r] を逆順にしたときの合計距離 new_score を求める
        # （現在の合計距離との差分を考える）
        new_score = current_score
        new_score -= dist_kk[P[l - 1]][P[l]]
        new_score -= dist_kk[P[r]][P[r + 1]]
        new_score += dist_kk[P[l - 1]][P[r]]
        new_score += dist_kk[P[l]][P[r + 1]]
        # 7.2 節の解答例から変更した唯一の部分（probability は採用確率）
        # （random.random() で 0 以上 1 未満のランダムな実数を生成）
        # T = 30 - 28 * (t / NUM_LOOPS)
        # probability = math.exp(min((current_score - new_score) / T, 0))
        # if random.random() < probability:
        if current_score > new_score:
            # 解が改善したときのみ P を更新する
            P[l:r+1] = reversed(P[l:r+1])
            current_score = new_score
        t += 1
    print("annealing", t, original_score, "->", new_score, *P, file=sys.stderr)
    return P


# すべての点間の最短距離を求めておく
dist_kk = []
for k in range(N * N):
    dist_kk.append(bfs_all_dist(k))
    # print("dist_kk", k, *dist_kk[k], file=sys.stderr)

# # ハブを求める
hub_list = create_hub_list()
print("hub_list", len(hub_list), *hub_list, file=sys.stderr)


ans = [0]

# 焼きなまし法
hub_route = simulated_annealing(hub_list, start=0, goal=-1)
print("hub route", *hub_route, file=sys.stderr)
# all_route = simulated_annealing(list(range(1, N*N)), start=0, goal=0)
# print("all route", *all_route, file=sys.stderr)

ans = route_cycle(ans, hub_route, start=0, goal=0, update_visited=False)   # まずハブを巡回して1周する
duty_route = ans.copy()
# ans = route_cycle(ans, hub_route, start=0, goal=0)   # まずハブを巡回して1周する
# ans = route_cycle(ans, all_route, start=0, goal=0)   # まずハブを巡回して1周する

# # 移動の推移を管理
ans = dfs(ans[-1])
# ans.extend(bfs(ans[-1], 0))
ans.extend(dijkstra(ans[-1], 0))
ans.extend(duty_route[1:])
# ans = remove_dup(ans)



# # ハブを含めながら追加のノードを巡回するルートを求める
# # while hub_dist_list:
# while visited_count < N * N:
#     if ans[-1] != hub_route[0]: # ハブの最初の点にいない場合はハブの最初の点まで移動
#         ans.extend(dijkstra(ans[-1], hub_route[0], update_visited=True))
#     # _dist_list, k = hub_dist_list.pop()
#     for _, k in calc_dust(ans):    # その時点の汚れが大きい順にハブ以外の点を選ぶ
#         # if not visited[k]: break # 未訪問の点
#         # if k not in hub_list[1:]: break # ハブ以外の点
#         if not visited[k] and k not in hub_list[1:]: break # 未訪問でハブ以外の点
#     _dist_list = hub_dist_list[k][0]
#     near_hub2 = [_dist_list[0][1], _dist_list[1][1]]  # 最も近いハブ2つ
#     # kと近傍のハブを含めたルートをtspで求める
#     idxs = []   # 最も近いハブ2つのidx
#     for i in range(len(hub_route)):
#         if hub_route[i] in near_hub2:
#             idxs.append(i)
#     print("near_hub2", k, near_hub2, idxs, file=sys.stderr)
#     _diff = idxs[1] - idxs[0]   # 最大8つまで，近傍ハブが同じ点を間に追加する
#     if _diff < 4:
#         for i in range(len(hub_route)):
#             if idxs[0] < i < idxs[1]:
#                 near_hub2.append(hub_route[i])
#         _route = list(hub_route[:idxs[0]+1])
#         # print(_route, idxs, file=sys.stderr)
#         _add_list = [k]
#         for i in range(len(sorted_hub_dist_list) - 2, -1, -1):
#             if visited[sorted_hub_dist_list[i][1]]:
#                 # sorted_hub_dist_list.pop(i)
#                 continue
#             if sorted_hub_dist_list[i][0][0][1] in near_hub2 and sorted_hub_dist_list[i][0][1][1] in near_hub2:
#             # if sorted_hub_dist_list[i][0][0][1] in near_hub2:
#                 _add_list.append(hub_dist_list[i][1])
#                 if len(_add_list) + _diff > 8: break
#         _node_list = list(hub_route[idxs[0]+1:idxs[1]]) + _add_list
#         _route.extend([_node_list[i-1] for i in tsp(hub_route[idxs[0]], hub_route[idxs[1]], node_list=_node_list)])
#         _route.extend(hub_route[idxs[1]:])
#     else:
#         for i in range(len(hub_route)):
#             if i < idxs[0] or idxs[1] < i:
#                 near_hub2.append(hub_route[i])
#         _route = list(hub_route[:idxs[1]+1])
#         _add_list = [k]
#         for i in range(len(sorted_hub_dist_list) - 2, -1, -1):
#             if visited[sorted_hub_dist_list[i][1]]:
#                 # sorted_hub_dist_list.pop(i)
#                 continue
#             if sorted_hub_dist_list[i][0][0][1] in near_hub2 and sorted_hub_dist_list[i][0][1][1] in near_hub2:
#                 _add_list.append(hub_dist_list[i][1])
#                 if len(_add_list) + 8 - _diff > 8: break
#         _node_list = list(hub_route[idxs[1]+1:]) + list(hub_route[:idxs[0]+1]) + _add_list
#         _route.extend([_node_list[i-1] for i in tsp(hub_route[idxs[1]], hub_route[idxs[0]], node_list=_node_list)])
#         _route.extend(hub_route[idxs[0]+1:])
#     print("add route", _add_list, _route, file=sys.stderr)
#     ans = route_cycle(ans, _route)
#     # print("ans", *ans, file=sys.stderr)
# ans.extend(dijkstra(hub_route[-1], 0, update_visited=True))

# # ans = route_cycle(ans, hub_route)


# # if calc_score(ans) < calc_score(ans[::-1]):
# #     print("reverse route", file=sys.stderr)
# #     ans = ans[::-1]
print_ans(ans)
# print("score =", calc_score(ans), file=sys.stderr)
# # print("reverse score =", calc_score(ans[::-1]), file=sys.stderr)
