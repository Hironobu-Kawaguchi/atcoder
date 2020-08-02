# https://atcoder.jp/contests/abc131/tasks/abc131_e
# import sys
# # input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

def main():
    n, k = map(int, input().split())
    mx = (n-1)*(n-2)//2
    if mx < k:
        print(-1)
        return
    ans = []
    for i in range(n-1):
        ans.append([i+1,n])     # star graph
    add = mx - k
    edge = []
    for i in range(n-1):
        for j in range(i):
            edge.append([i+1, j+1]) # complete graph
    for i in range(add):
        ans.append(edge[i])         # add本のedgeを追加
    m = len(ans)
    print(m)
    for i in range(m):
        print(*ans[i])

main()



# # import numpy as np
# from itertools import product
# INF = 1001001001
# from scipy.sparse.csgraph import floyd_warshall, csgraph_from_dense
# N, K = map(int, input().split())

# G = [[INF] * N for _ in range(N)]
# for i, j in product(range(N), repeat=2):
#     # print(i,j)
#     if i == j:
#         G[i][j] = 0
#     if (i+1==j) or (i==N-1 and j==0):
#         G[i][j] = 1
#         G[j][i] = 1
# G = floyd_warshall(csgraph_from_dense(G))
# # print(G)

# def count_k(G):
#     res = 0
#     for i, j in product(range(N), repeat=2):
#         if G[i][j] == 2:
#             res += 1
#     return res // 2

# # print(count_k(G))

# while count_k(G) != K:
#     for i, j in product(range(N), repeat=2):
#         if G[i][j] > 1.5:
#             G[i][j] = G[j][i] = 1.
#             break

# def print_g(G):
#     ans = []
#     for i, j in product(range(N), repeat=2):
#         if i<j and G[i][j] == 1.:
#             ans.append([i,j])
#     print(len(ans))
#     for u, v in ans:
#         print(u, v)

# # print(count_k(G))
# # print(G)
# print_g(G)
