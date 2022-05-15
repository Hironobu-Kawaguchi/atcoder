# https://atcoder.jp/contests/ABC214/tasks/abc214_c

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = list(map(int, (input().split())))
T = list(map(int, (input().split())))
for i in range(2*N):
    T[(i+1)%N] = min(T[(i+1)%N], T[i%N] + S[i%N])
for i in range(N):
    print(T[i])


# import heapq
# N = int(input())
# S = list(map(int, (input().split())))
# T = list(map(int, (input().split())))
# ans = [-1] * N
# cnt = 0
# q = []
# for i in range(N):
#     heapq.heappush(q, (T[i], i))
# while cnt<N:
#     t, i = heapq.heappop(q)
#     if ans[i] != -1: continue
#     ans[i] = t
#     cnt += 1
#     if ans[(i+1)%N] == -1:
#         heapq.heappush(q, (t+S[i], (i+1)%N))
# for i in range(N):
#     print(ans[i])


# INF = 1001001001
# N = int(input())
# S = list(map(int, (input().split())))
# S = S+S
# # print(S)
# cumS = [0]
# for s in S:
#     cumS.append(cumS[-1]+s)
# # print(cumS)
# T = list(map(int, (input().split())))
# Tidx = [(t, i) for i, t in enumerate(T)]
# Tidx.sort()
# # print(T)
# ans = [INF]*N
# for t, i in Tidx:
#     if ans[i]<=t: continue
#     ans[i] = t
#     for j in range(N-1):
#         if ans[(i+j+1)%N] < ans[(i+j)%N] + S[(i+j)%N]: break
#         ans[(i+j+1)%N] = ans[(i+j)%N] + S[(i+j)%N]

# for i in range(N):
#     print(ans[i])

