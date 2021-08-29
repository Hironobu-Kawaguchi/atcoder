# https://atcoder.jp/contests/abc216/tasks/abc216_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
A = list(map(int, (input().split())))

def calc_tot(now):
    tot = 0
    for i in range(N):
        tot += max(A[i]-now, 0)
    return tot

l, r = 0, 2001001001
while l+1<r:
    now = (l+r)//2
    tot = calc_tot(now)
    if tot>K:
        l = now
    else:
        r = now
tot = calc_tot(l)
if tot>K:
    l = r

# print(l, r)
ans = 0
for i in range(N):
    if A[i]>l:
        ans +=(A[i]+l+1) * (A[i]-l) // 2
        K -= A[i]-l
ans += K * l
print(ans)


# # TLE
# import heapq

# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
# q = []
# for i in range(N):
#     heapq.heappush(q, -A[i])
# # print(q)
# ans = 0
# for k in range(K):
#     v = heapq.heappop(q)
#     if v>=0: break
#     ans -= v
#     heapq.heappush(q, v+1)
# print(ans)


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
