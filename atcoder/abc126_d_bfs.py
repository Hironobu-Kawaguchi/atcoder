# D - Even Relation
# https://atcoder.jp/contests/abc126/tasks/abc126_d

from collections import deque
N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):    # 辺はN-1本
    u, v, w = map(int, input().split())
    G[u-1].append((v-1, w)) # GにGraph情報を格納(直接結合している頂点と距離)
    G[v-1].append((u-1, w))

used = [0] * N
used[0] = 1
q = deque([0])  # u=0 から開始
ans = [0] * N

while q:    # qがある間ループ
    u = q.popleft()
    color = ans[u]
    for v, w in G[u]:   # uに直接結合している頂点(v)と距離(w)
        if used[v]:
            continue
        if w % 2:   # 奇数ならuとvは別の色
            ans[v] = 1 - color
        else:       # 偶数ならuとvは同じ色
            ans[v] = color
        q.append(v) # 幅優先探索
        used[v] = 1

for i in range(N):
    print(ans[i])


# from collections import deque
# N = int(input())

# u, v, w = [], [], []
# ans = [0] * N

# for i in range(N-1):
#     _u, _v, _w = map(int, input().split())
#     u.append(_u)
#     v.append(_v)
#     w.append(_w)
# # print(u)
# # print(v)
# # print(w)

# flg = w[0] % 2
# ans[v[0]-1] ^= flg
# q = deque([(u[0], v[0], w[0], ans[v[0]-1])])
# # print(q)

# s = set()
# s.add((u[0], v[0], w[0]))
# # print(s)

# while q:
#     u_, v_, w_, ans_ = q.popleft()
#     for i in range(1, N-1):
#         if u[i] == v_ and ((u[i], v[i], w[i]) not in s):
#             flg = w[i] % 2
#             s.add((u[i], v[i], w[i]))
#             q.append((u[i], v[i], w[i], ans_ ^ flg))
#             ans[v[i]-1] = ans_ ^ flg
#         if v[i] == v_ and ((u[i], v[i], w[i]) not in s):
#             flg = w[i] % 2
#             s.add((u[i], v[i], w[i]))
#             q.append((u[i], v[i], w[i], ans_ ^ flg))
#             ans[u[i]-1] = ans_ ^ flg

# for i in range(N):
#     print(ans[i])
