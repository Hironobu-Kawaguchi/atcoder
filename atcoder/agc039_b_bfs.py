# https://atcoder.jp/contests/agc039/tasks/agc039_b
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

from collections import deque

N = int(input())
S = [input() for _ in range(N)]

def bfs(start):
    res = 0
    dist = [-1] * N
    dist[start] = 1
    q = deque()
    q.append([start, 1])
    st = set()
    st.add((start, 1))

    while q:
        i, d = q.popleft()
        if dist[i] == -1:
            dist[i] = d
            res = max(res, d)
        elif dist[i] != d:
            res = -1
            break
        for j in range(N):
            if S[i][j] == '1' and dist[j] != d-1:
                if (j, d+1) not in st:
                    q.append([j, d+1])
                    st.add((j, d+1))
    return res

ans = -1
for i in range(N):
    k = bfs(i)
    if k == -1:
        break
    else:
        ans = max(ans, k)

print(ans)


# TLE
# import sys
# # input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

# INF = 1001001001
# from scipy.sparse.csgraph import floyd_warshall
# from collections import deque

# N = int(input())
# S = [input() for _ in range(N)]
# G = [[INF]*N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             G[i][j] = 0
#         elif S[i][j] == '1':
#             G[i][j] = 1
# # print(G)

# dist = floyd_warshall(G)
# # print(dist)

# k_1 = 0
# for i in range(N):
#     for j in range(N):
#         if int(dist[i][j]) > k_1:
#             k_1 = int(dist[i][j])
#             max_i = i
#             max_j = j
# k = k_1 + 1

# dist = [-1] * N
# dist[max_i] = 1
# q = deque()
# q.append([max_i, 1])

# while q:
#     i, d = q.popleft()
#     if dist[i] == -1:
#         dist[i] = d
#     elif dist[i] != d:
#         k = -1
#         break
#     for j in range(N):
#         if S[i][j] == '1' and dist[j] != d-1:
#             q.append([j, d+1])

# print(k)
