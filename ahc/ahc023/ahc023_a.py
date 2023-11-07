# https://atcoder.jp/contests/ahc023/tasks/asprocon10_a
import sys
from collections import deque
from typing import List, Tuple, NamedTuple

class Work(NamedTuple):
    k: int
    i: int
    j: int
    s: int

def read_input():
    global T, K, H, W, i0, h, v, S, D
    T, H, W, i0 = map(int, input().split())
    
    h = []
    for _ in range(H - 1):
        row = list(map(int, input().strip()))
        h.append(row)

    v = []
    for _ in range(H):
        row = list(map(int, input().strip()))
        v.append(row)

    K = int(input())
    S, D = [], []
    for _ in range(K):
        s, d = map(int, input().split())
        S.append(s)
        D.append(d)

def reachable(i: int, j: int, adj: List[List[List[Tuple[int, int]]]], used: List[List[bool]]) -> bool:
    global i0, H, W

    if used[i][j] or used[i0][0]:
        return False
    if i == i0 and j == 0:
        return True
    
    q = deque([(i0, 0)])
    visited = [[False for _ in range(W)] for _ in range(H)]
    visited[i0][0] = True

    while q:
        i1, j1 = q.popleft()
        for i2, j2 in adj[i1][j1]:
            if i2 == i and j2 == j:
                return True
            if not used[i2][j2] and not visited[i2][j2]:
                visited[i2][j2] = True
                q.append((i2, j2))

    return False

def is_valid_plan(plan: List[Work], adj: List[List[List[Tuple[int, int]]]]) -> bool:
    global H, W, T, D, S

    plant_list = [[] for _ in range(T + 1)]
    harvest_list = [[] for _ in range(T + 1)]

    for w in plan:
        plant_list[w.s].append(w)
        harvest_list[D[w.k]].append(w)
    
    used = [[False for _ in range(W)] for _ in range(H)]
    
    for t in range(1, T + 1):
        for w in plant_list[t]:
            if not reachable(w.i, w.j, adj, used):
                return False
        
        for w in plant_list[t]:
            if used[w.i][w.j]:
                return False
            used[w.i][w.j] = True

        for w in harvest_list[t]:
            used[w.i][w.j] = False

        for w in harvest_list[t]:
            if not reachable(w.i, w.j, adj, used):
                return False
    
    return True

if __name__ == '__main__':
    read_input()
    
    adj = [[[] for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if i + 1 < H and not h[i][j]:
                adj[i][j].append((i + 1, j))
                adj[i + 1][j].append((i, j))

            if j + 1 < W and not v[i][j]:
                adj[i][j].append((i, j + 1))
                adj[i][j + 1].append((i, j))

    cells = []
    q = deque([(i0, 0)])
    visited = [[False for _ in range(W)] for _ in range(H)]
    visited[i0][0] = True

    while q:
        i, j = q.popleft()
        cells.append((i, j))
        for i2, j2 in adj[i][j]:
            if not visited[i2][j2]:
                visited[i2][j2] = True
                q.append((i2, j2))
    
    plan = []
    l = len(cells) - 1

    for k in range(K):
        found = False
        while l >= 0 and not found:
            i, j = cells[l]
            w = Work(k, i, j, S[k])
            plan.append(w)

            if not is_valid_plan(plan, adj):
                plan.pop()
            else:
                found = True

            l -= 1

    score = 0
    for w in plan:
        score += D[w.k] - S[w.k] + 1
    
    score *= 1000000
    score //= (H * W * T)
    
    print("score:", score, file=sys.stderr)
    
    print(len(plan))
    for w in plan:
        print(f"{w.k + 1} {w.i} {w.j} {w.s}")
