# https://atcoder.jp/contests/ahc004/tasks/ahc004_a

# import copy
# import random
# import time
# from collections import deque
# from collections import defaultdict

# INF = 1001001001
# vi = [-1, 1, 0, 0]
# vj = [ 0, 0,-1, 1]
# directions = ['U', 'D', 'L', 'R']
# start = time.time()

N, M, T = map(int, input().split())
ans = [[-1, -1]] * T
vegitables = []
for i in range(M):
    R, C, S, E ,V = map(int, input().split())
    vegitables.append([V, T-(E-S+1), R, C, S-1, E])
vegitables.sort(reverse=True)
for i in range(M):
    for t in range(vegitables[i][4], vegitables[i][5]):
        if ans[t]==[-1, -1]:
            ans[t] = [vegitables[i][2], vegitables[i][3]]
            break

now = [-1, -1]
for t in range(T):
    if ans[t]==[-1, -1]:
        print(-1)
    else:
        if now==[-1, -1]:
            print(*ans[t])
        else:
            print(*now, *ans[t])
        now = ans[t]


# map = [list(input().rstrip()) for _ in range(N)]
# r = 0
# for i in range(N):
#     for j in range(N):
#         if map[i][j]!='#':
#             r += 1
# newmap = copy.deepcopy(map)

# # end cut
# flag = False
# for i in range(N):
#     if i==si: continue
#     for j in range(N):
#         if map[i][j]=='#': continue
#         if not flag and j>0 and map[i][j-1]!='#':continue
#         if i>0 and map[i-1][j]!='#':
#             flag = False
#             continue
#         if i<N-1 and map[i+1][j]!='#':
#             flag = False
#             continue
#         flag = True
#         newmap[i][j] = '#'
# flag = False
# for i in range(N):
#     if i==si: continue
#     for j in range(N-1, -1, -1):
#         if map[i][j]=='#': continue
#         if not flag and j<N-1 and map[i][j+1]!='#':continue
#         if i>0 and map[i-1][j]!='#':
#             flag = False
#             continue
#         if i<N-1 and map[i+1][j]!='#':
#             flag = False
#             continue
#         flag = True
#         newmap[i][j] = '#'
# flag = False
# for j in range(N):
#     if j==sj: continue
#     for i in range(N):
#         if map[i][j]=='#': continue
#         if not flag and i>0 and map[i-1][j]!='#':continue
#         if j>0 and map[i][j-1]!='#':
#             flag = False
#             continue
#         if j<N-1 and map[i][j+1]!='#':
#             flag = False
#             continue
#         flag = True
#         newmap[i][j] = '#'
# flag = False
# for j in range(N):
#     if j==sj: continue
#     for i in range(N-1, -1, -1):
#         if map[i][j]=='#': continue
#         if not flag and i<N-1 and map[i+1][j]!='#':continue
#         if j>0 and map[i][j-1]!='#':
#             flag = False
#             continue
#         if j<N-1 and map[i][j+1]!='#':
#             flag = False
#             continue
#         flag = True
#         newmap[i][j] = '#'

# # for i in range(N):
# #     print(map[i])
# # for i in range(N):
# #     print(newmap[i])

# def reverse_direction(direction):
#     if direction==0:
#         return 1
#     elif direction==1:
#         return 0
#     elif direction==2:
#         return 3
#     elif direction==3:
#         return 2
#     return direction

# def choice_direction(direction, i, j):
#     available_direction = []
#     weights = []
#     for k in range(4):
#         ni = i + vi[k]
#         if ni>=N or ni<0: continue
#         nj = j + vj[k]
#         if nj>=N or nj<0: continue
#         if newmap[ni][nj]=='#': continue
#         # if map[ni][nj]=='#': continue
#         available_direction.append(k)
#         weights.append(5*6*7*8*9//int(map[ni][nj]))
#     if len(available_direction)==1:    ### dead end
#         direction = available_direction[0]
#     # elif len(available_direction)==2:
#     #     if reverse_direction(direction) in available_direction:
#     #         available_direction.remove(reverse_direction(direction))
#     #     direction = random.choice(available_direction)
#     else:
#         x = 0
#         while x<len(available_direction):
#             if reverse_direction(direction)==available_direction[x]:
#                 available_direction.pop(x)
#                 weights.pop(x)
#             else:
#                 x += 1
#         direction = random.choices(available_direction, k=1, weights=weights)[0]
#     ni = i + vi[direction]
#     nj = j + vj[direction]
#     return direction, ni, nj

# # def check_gone(gone):
# #     seen = copy.deepcopy(gone)
# #     flag = False
# #     for i in range(N):
# #         flag = False
# #         for j in range(N):
# #             if gone[i][j]: flag = True
# #             if map[i][j]=='#': flag = False
# #             if flag:
# #                 seen[i][j] = True
# #     flag = False
# #     for i in range(N):
# #         flag = False
# #         for j in range(N-1, -1, -1):
# #             if gone[i][j]: flag = True
# #             if map[i][j]=='#': flag = False
# #             if flag:
# #                 seen[i][j] = True
# #     flag = False
# #     for j in range(N):
# #         flag = False
# #         for i in range(N):
# #             if gone[i][j]: flag = True
# #             if map[i][j]=='#': flag = False
# #             if flag:
# #                 seen[i][j] = True
# #     flag = False
# #     for j in range(N):
# #         flag = False
# #         for i in range(N-1, -1, -1):
# #             if gone[i][j]: flag = True
# #             if map[i][j]=='#': flag = False
# #             if flag:
# #                 seen[i][j] = True
# #     v = 0
# #     for i in range(N):
# #         for j in range(N):
# #             if seen[i][j]:
# #                 v += 1
# #     return v

# def seen_update(direction, i, j, v, seen):
#     if not seen[i][j]:
#         v += 1
#         seen[i][j] = True
#     for k in range(4):
#         if k==direction: continue
#         if k==reverse_direction(direction): continue
#         ni, nj = i, j
#         while True:
#             ni = ni + vi[k]
#             if ni>=N or ni<0: break
#             nj = nj + vj[k]
#             if nj>=N or nj<0: break
#             if map[ni][nj]=='#': break
#             if not seen[ni][nj]:
#                 v += 1
#                 seen[ni][nj] = True
#     return v, seen

# def dijkstra(ni, nj, ans, cost):
#     import heapq
#     dist = [[INF]*N for _ in range(N)]
#     dist[ni][nj] = 0
#     # q = deque([(ni, nj, 0, [])])
#     q = []
#     heapq.heappush(q, (0, ni, nj, list()))

#     while len(q)>0:
#         # i, j, d, route = q.popleft()
#         d, i, j, route = heapq.heappop(q)
#         # print(route)
#         if i==si and j==sj:
#             ans.extend(route)
#             cost += d
#         # print(i,j,d)
#         for k in range(4):
#             ni = i + vi[k]
#             if ni>=N or ni<0: continue
#             nj = j + vj[k]
#             if nj>=N or nj<0: continue
#             if map[ni][nj]=='#': continue
#             if dist[ni][nj]!=INF: continue
#             dist[ni][nj] = d+int(map[ni][nj])
#             # q.append((ni, nj, d+int(map[ni][nj]), route.append(directions[k])))
#             heapq.heappush(q, (d+int(map[ni][nj]), ni, nj, route + list(directions[k])))
#     # for i in range(N):
#     #     print(dist[i])
#     return ans, cost

# def solve():
#     ans = []
#     cost = 0
#     # gone = [[False]*N for _ in range(N)]
#     # gone[si][sj] = True
#     seen = [[False]*N for _ in range(N)]
#     v = 0
#     v, seen = seen_update(-1, si, sj, v, seen)
#     direction, ni, nj = choice_direction(-1, si, sj)
#     ans.append(directions[direction])
#     cost += int(newmap[ni][nj])
#     # cost += int(map[ni][nj])
#     while ni!=si or nj!=sj:
#         # gone[ni][nj] = True
#         v, seen = seen_update(direction, ni, nj, v, seen)
#         if r==v:   #### all seen then back to start point by dijkstra
#             ans, cost = dijkstra(ni, nj, ans, cost)
#             break
#         direction, ni, nj = choice_direction(direction, ni, nj)
#         ans.append(directions[direction])
#         cost += int(newmap[ni][nj])
#         # cost += int(map[ni][nj])
#     # v = check_gone(gone)
#     return ans, cost, v

# best_ans = []
# best_score = 0
# while time.time() < start + 2.8:
# # while time.time() < start + 0.2:
#     ans, cost, v = solve()
#     if r==v:
#         score = (10**4) + (10**7) * N / cost
#     else:
#         score = (10**4) * v / r
#     if score>best_score:
#         best_ans = ans
#         best_score = score
#         # print(r,v, best_score)

# print(''.join(best_ans))
# # print(best_score)


# # # all connected
# # for i in range(N):
# #     for j in range(N):
# #         if map[i][j]!='#' and dist[i][j]==INF:
# #             print("not connect", i, j)
