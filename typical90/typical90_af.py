# https://atcoder.jp/contests/typical90/tasks/typical90_af

import sys
input = sys.stdin.buffer.readline
import itertools
sys.setrecursionlimit(10 ** 7)
INF = 1001001001

N = int(input())
A = [[int(i) for i in input().split()] for _ in range(N)]
M = int(input())
dame = [set() for _ in range(N)]
for i in range(M):
    X, Y = map(int, input().split())
    X -= 1; Y -= 1
    dame[X].add(Y)
    dame[Y].add(X)

ans = INF

for it in itertools.permutations(range(N), N):
    sm = 0
    flag = True
    for j, i in enumerate(it):
        if j!=0 and i in dame[it[j-1]]:
            flag = False
        sm += A[i][j]
    if flag: ans = min(ans, sm)

if ans!=INF:
    print(ans)
else:
    print(-1)


# WA
# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
# INF = 1001001001

# N = int(input())
# A = [[int(i) for i in input().split()] for _ in range(N)]
# M = int(input())
# dame = [set() for _ in range(N)]
# for i in range(M):
#     X, Y = map(int, input().split())
#     X -= 1; Y -= 1
#     dame[X].add(Y)
#     dame[Y].add(X)

# ans = INF

# def dfs(j: int, i: int, point: int, st: set):
#     if i!=-1:
#         point += A[i][j]
#         if j==N-1:
#             global ans
#             ans = min(ans, point)
#             return
#     for k in range(N):
#         if k in st: continue
#         if i!=-1 and k in dame[i]: continue
#         st.add(k)
#         dfs(j+1, k, point, st)
#     return

# dfs(-1, -1, 0, set())
# if ans!=INF:
#     print(ans)
# else:
#     print(-1)


