# https://atcoder.jp/contests/abc318/tasks/abc318_d
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
# D = [list(map(int, input().split())) for _ in range(N)]
D = [[0]*(N+1) for _ in range(N+1)]
for i in range(N-1):
    _d = list(map(int, input().split()))
    for j in range(N-i-1):
        D[i][i+j+1] = _d[j]
        D[i+j+1][i] = _d[j]
# print(D, file=sys.stderr)
if N%2:
    N += 1

used = [False] * N

def dfs():
    if all(used):
        return 0
    ret = 0
    u = used.index(False)
    for v in range(u+1, N):
        if not used[v]:
            used[u] = used[v] = True
            ret = max(ret, D[u][v] + dfs())
            used[u] = used[v] = False
    return ret

ans = dfs()
print(ans)


# https://atcoder.jp/contests/abc318/editorial/7076
# N = int(input())
# D = [[0 for j in range(N)] for i in range(N)]
# for i in range(N - 1):
#     d = list(map(int, input().split()))
#     for j in range(i + 1, N):
#         D[i][j] = D[j][i] = d[j - i - 1]

# def dfs(used):
#     if all(used):
#         return 0
#     v = used.index(False)
#     used[v] = True
#     ret = 0
#     for w in range(v + 1, N):
#         if not used[w]:
#             used[w] = True
#             ret = max(ret, D[v][w] + dfs(used))
#             used[w] = False
#     used[v] = False
#     return ret


# used = [False] * N
# ans = 0
# if N % 2 == 0:
#     ans = dfs(used)
# else:
#     for v in range(N):
#         used[v] = True
#         ans = max(ans, dfs(used))
#         used[v] = False
# print(ans)
