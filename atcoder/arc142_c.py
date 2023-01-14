# https://atcoder.jp/contests/arc142/tasks/arc142_c

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
# from collections import deque
INF = 1001001

def main():
    N = int(input())
    dist = [[INF]*N for _ in range(2)]

    for u in range(2):
        for v in range(2, N):
            print('?', u+1, v+1, flush=True)
            d = int(input())
            if d==-1:
                return
            dist[u][v] = d

    ans = INF
    lst = []
    for v in range(2, N):
        d = dist[0][v] + dist[1][v]
        if d==3:
            lst.append(v)
        ans = min(ans, d)
    if ans!=3:
        print('!', ans)
    else:
        if len(lst)!=2:
            print('!', 1)
        else:
            print('?', lst[0]+1, lst[1]+1, flush=True)
            d = int(input())
            if d==1:
                print('!', 3)
            else:
                print('!', 1)
    return

main()


# WA
# import sys
# input = sys.stdin.buffer.readline
# # sys.setrecursionlimit(10 ** 7)
# from collections import deque

# N = int(input())
# G = [[] for _ in range(N)]

# M = 0
# for u in range(N):
#     for v in range(u+1, N):
#         if u+v==1: continue
#         print('?', u+1, v+1, flush=True)
#         d = int(input())
#         if d==1:
#             G[u].append(v)
#             G[v].append(u)
#             M += 1
#         elif d==-1:
#             exit()

# if M+1==N:
#     q = deque([(0, 0)])
#     visited = [False] * N
#     visited[0] = True
#     while q:
#         u, d = q.popleft()
#         if u==1:
#             print('!', d)
#             break
#         for v in G[u]:
#             if visited[v]: continue
#             visited[v] = True
#             q.append((v, d+1))
# else:
#     print('!', 1)
