# https://atcoder.jp/contests/ahc006/tasks/ahc006_a
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
import random
import time
start = time.time()
from collections import Counter
import heapq

ab = []
cd = []
for i in range(1000):
    a, b, c, d = map(int, input().split())
    ab.append((a,b))
    cd.append((c,d))
m = 50

# print(ab+cd)
cnt = Counter(ab+cd)
# print(cnt)
same_cnt = [0]*1000
for i in range(1000):
    same_cnt[i] += cnt[ab[i]]
    same_cnt[i] += cnt[cd[i]]
cnt_idx = []
for i in range(1000):
    cnt_idx.append((same_cnt[i], i))
cnt_idx.sort(reverse=True)
# print(cnt_idx)
prechoice = []
nochoice = []
for i in range(1000):
    if len(prechoice)<=45 and cnt_idx[i][0]>=3:
        prechoice.append(cnt_idx[i][1]+1)
    else:
        nochoice.append(cnt_idx[i][1]+1)
# print(len(prechoice)+len(nochoice), len(prechoice), prechoice)


def mst(choice, sx, sy):
    min_cost = 1001001001
    best_idx = -1
    for i in range(m):
        cost = abs(choice[i][0]-sx) + abs(choice[i][1]-sy)
        if cost<min_cost:
            min_cost = cost
            best_idx = i
    q = [(min_cost, best_idx, 0)]    # (cost, idx, pre_idx)
    heapq.heapify(q)
    visited = [0] * m
    connection = 0
    G = [[] for _ in range(m+1)]
    while len(q):
        cost, v, u = heapq.heappop(q)
        if visited[v]:
            continue
        # そのノードと繋げる
        visited[v] = 1
        connection += 1
        G[u].append(v)
        G[v].append(u)
        # 新たに繋げたノードから行けるところをエンキュー
        for j in range(50):
            if j==v: continue
            cost = abs(choice[v][0]-choice[j][0]) + abs(choice[v][1]-choice[j][1])
            heapq.heappush(q, (cost, j, v))

        # 全部のノードが繋がったら終了
        if connection == m:
            break
    return G



def route(G, abcd=ab):
    st = set((400,400))
    visited = [0] * m
    cnt = [0]
    now = G[0][0]
    ans_extend = [abcd[now][0], abcd[now][1]]

    def dfs(v):
        if cnt[0]==m: return
        if visited[v]==0:
            visited[v] = 1
            cnt[0] += 1
        return    

    while cnt[0]<m:
        for v in G[now]:
            dfs(v)

        if (ab[choice[i]-1][0], ab[choice[i]-1][1]) in st: continue
        ans.append(ab[choice[i]-1][0])
        ans.append(ab[choice[i]-1][1])
        st.add((ab[choice[i]-1][0], ab[choice[i]-1][1]))
    return ans_extend


def solve():
    # choice = list(range(1, m+1))
    # choice = random.sample(list(range(1, 1001)), m)
    choice = prechoice + random.sample(nochoice, m-len(prechoice))
    # choice = random.sample(choice, m)
    ans = [400,400]

    ab_choice = [ab[i-1] for i in choice]
    ab_G = mst(ab_choice, 400, 400)

    cd_choice = [cd[i-1] for i in choice]
    st = set((400,400))
    for i in range(m):
        if (cd[choice[i]-1][0], cd[choice[i]-1][1]) in st: continue
        ans.append(cd[choice[i]-1][0])
        ans.append(cd[choice[i]-1][1])
        st.add((cd[choice[i]-1][0], cd[choice[i]-1][1]))

    ans.extend([400, 400])
    
    T = 0
    for i in range(len(ans)//2-1):
        T += abs(ans[(i+1)*2]-ans[i*2]) + abs(ans[(i+1)*2+1]-ans[i*2+1])
        
    return choice, ans, T


best_ans = []
best_choice = []
best_T = 1001001001
while time.time() < start + 1.0:
    choice, ans, T = solve()
    if T<best_T:
        best_choice = choice
        best_ans = ans
        best_T = T
        # print(T, time.time()-start)

# print(len(set(best_choice)))
# best_choice.sort()
print(m, *best_choice)
print(len(best_ans)//2, *best_ans)
