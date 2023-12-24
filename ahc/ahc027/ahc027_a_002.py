# https://atcoder.jp/contests/ahc027/tasks/ahc027_a
import sys
from collections import deque
sys.setrecursionlimit(1000000)

# 入力
N = int(input())
h = [input() for _ in range(N-1)]
v = [input() for _ in range(N)]
d = [list(map(int, input().split())) for _ in range(N)]

# Graphにする　k = i * N + j
G = [[] for _ in range(N * N)]
for i in range(N):
    for j in range(N):
        k = i * N + j
        if i < N - 1:
            if h[i][j] == '0':
                k2 = (i + 1) * N + j
                G[k].append((k2, 1))    # D
                G[k2].append((k, 3))    # U
        if j < N - 1:
            if v[i][j] == '0':
                k2 = i * N + j + 1
                G[k].append((k2, 0))    # R
                G[k2].append((k, 2))    # L

# 移動の管理
visited = [False for _ in range(N*N)]
visited_count = 0
DIJ = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIR = "RDLU"

# 移動の推移を管理
ans = [0]

# DFS
def dfs(k):
    global visited_count
    # print("visited count", visited_count, k, file=sys.stderr)
    if visited_count >= N * N: return
    if not visited[k]: visited_count += 1
    visited[k] = True
    dirs = []
    for k2, dir in G[k]:
        if not visited[k2]:
            dirs.append((len(G[k2]), k2, dir))
    dirs.sort()
    for _, k2, dir in dirs:
        if not visited[k2]:
            ans.append(k2)  # 往路
            dfs(k2)
            if visited_count < N * N:
                ans.append(k)   # 復路
    return

# BFSで最短経路を求める
def bfs(start, goal):
    print("start bfs", start, goal, file=sys.stderr)
    dist = [-1 for _ in range(N*N)]
    q = deque([(start, 0)])
    while q:
        k, d = q.popleft()
        if dist[k] != -1: continue
        dist[k] = d
        if k == goal: break
        for k2, _ in G[k]:
            if dist[k2] == -1:  # 未訪問
                q.append((k2, d + 1))
    print("start route search", start, goal, file=sys.stderr)
    route = []
    now = goal
    while now != start:
        route.append(now)
        for k2, dir in G[now]:
            if dist[k2] == dist[now] - 1:
                now = k2
                break
    return route[::-1]

# 重複する移動を削除
def remove_dup(ans):
    # 累積和で区間の到達回数を管理
    cum = [[0 for _ in range(N * N)] for _ in range(len(ans) + 1)]
    for i in range(len(ans)):
        for j in range(N * N):
            cum[i+1][j] = cum[i][j]
        cum[i+1][ans[i]] += 1
    now = len(ans) - 1
    while now > 0:
        if cum[now][ans[now]] > 1:  # nowより前に既に到達している
            pre = now - 1
            while pre > 0 and ans[pre] != ans[now]: # 前回到達した時
                pre -= 1
            # print("remove dup check", now, pre, file=sys.stderr)
            ok = True
            for k in range(N * N):  # pre と now の間に到達したすべての場所をその前に既に到達しているか確認
                if cum[now][k] - cum[pre + 1][k] > 0:
                    if cum[pre][k] == 0:    # 到達していない
                        ok = False
                        break
            if ok:
                print("remove dup", now, pre, file=sys.stderr)
                ans = ans[:pre] + ans[now:]
                now = pre
            else:
                now -= 1
        else:
            now -= 1

# 移動の推移から回答を出力
def print_ans(ans):
    for i in range(len(ans) - 1):
        k = ans[i]
        k2 = ans[i+1]
        if k2 - k == 1:
            print("R", end='')
        elif k2 - k == -1:
            print("L", end='')
        elif k2 - k == N:
            print("D", end='')
        else:
            print("U", end='')
    print()

dfs(0)
ans.extend(bfs(ans[-1], 0))
remove_dup(ans)
print_ans(ans)
