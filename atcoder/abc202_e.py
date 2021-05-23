# https://atcoder.jp/contests/abc202/tasks/abc202_e

import sys
import bisect
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

def main():
    N = int(input())
    P = list(map(int, (input().split())))
    G = [[] for _ in range(N)]
    depth   = [-1] * N
    in_num  = [-1] * N
    out_num = [-1] * N
    k = 0
    ls = [[] for _ in range(N)]
    for i in range(N-1):
        G[P[i]-1].append(i+1)
        # G[i+1].append(P[i]-1)

    def dfs(now, d, G, depth, k, in_num, out_num):
        in_num[now] = k
        k += 1
        depth[now] = d
        for next in G[now]:
            # if depth[next]!=-1: continue
            k = dfs(next, d+1, G, depth, k, in_num, out_num)
        out_num[now] = k
        return k

    dfs(0, 0, G, depth, k, in_num, out_num)
    for i in range(N):
        ls[depth[i]].append(in_num[i])
        # print(i, depth[i], in_num[i], out_num[i])
    for i in range(N):
        ls[i].sort()
        # print(i, ls[i])

    Q = int(input())
    for qi in range(Q):
        U, D = map(int, input().split())
        U -= 1
        ans = bisect.bisect_left(ls[D], out_num[U]) - bisect.bisect_left(ls[D], in_num[U])
        print(ans)
    return

main()


# def main():
#     N = int(input())
#     P = list(map(int, (input().split())))
#     G = [[] for _ in range(N)]
#     depth = [-1 for _ in range(N)]
#     child = [set() for _ in range(N)]
#     for i in range(N-1):
#         G[P[i]-1].append(i+1)
#         G[i+1].append(P[i]-1)

#     def dfs(now, d, G, depth, child):
#         depth[now] = d
#         child_set = set([now])
#         for next in G[now]:
#             if depth[next]!=-1: continue
#             child_set |= dfs(next, d+1, G, depth, child)
#         child[now] |= child_set
#         return child_set

#     child[0] |= dfs(0, 0, G, depth, child)
#     # for i in range(N):
#     #     print(i, depth[i], child[i])

#     Q = int(input())
#     for qi in range(Q):
#         U, D = map(int, input().split())
#         ans = 0
#         for i in child[U-1]:
#             if depth[i] == D:
#                 ans += 1
#         print(ans)
#     return

# main()


