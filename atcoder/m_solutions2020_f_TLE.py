# https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_f
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()

# import sys
# input = sys.stdin.buffer.readline

from itertools import combinations
d = {'U':0, 'D':1, 'L':2, 'R':3}
N = int(input())
xy = [[[] for _ in range(200001)] for _ in range(4)]
xpy = [[[] for _ in range(400001)] for _ in range(4)]
xmy = [[[] for _ in range(400001)] for _ in range(4)]
lst = []
ans = 1001001001
for i in range(N):
    x, y, u = input().split()
    x = int(x)
    y = int(y)
    lst.append((x,y,u))
    if u == 'U':
        xy[d[u]][x].append(i)
        for j in xy[d['D']][x]:
            if lst[j][1] > y:
                ans = min(ans, lst[j][1] - y)
        xpy[d[u]][x+y].append(i)
        for j in xpy[d['R']][x+y]:
            if lst[j][0] < x:
                ans = min(ans, (x - lst[j][0])*2)
        xmy[d[u]][x-y+20000].append(i)
        for j in xmy[d['L']][x-y+20000]:
            if lst[j][0] > x:
                ans = min(ans, (lst[j][0]-x)*2)
    elif u == 'D':
        xy[d[u]][x].append(i)
        for j in xy[d['U']][x]:
            if lst[j][1] < y:
                ans = min(ans, y - lst[j][1])
        xpy[d[u]][x+y].append(i)
        for j in xpy[d['L']][x+y]:
            if lst[j][0] > x:
                ans = min(ans, (lst[j][0]-x)*2)
        xmy[d[u]][x-y+20000].append(i)
        for j in xmy[d['R']][x-y+20000]:
            if lst[j][0] < x:
                ans = min(ans, (x-lst[j][0])*2)
    elif u == 'R':
        xy[d[u]][y].append(i)
        for j in xy[d['L']][y]:
            if lst[j][0] > x:
                ans = min(ans, lst[j][0] - x)
        xpy[d[u]][x+y].append(i)
        for j in xpy[d['U']][x+y]:
            if lst[j][0] > x:
                ans = min(ans, (lst[j][0]-x)*2)
        xmy[d[u]][x-y+20000].append(i)
        for j in xmy[d['D']][x-y+20000]:
            if lst[j][0] > x:
                ans = min(ans, (lst[j][0]-x)*2)
    elif u == 'L':
        xy[d[u]][y].append(i)
        for j in xy[d['R']][y]:
            if lst[j][0] < x:
                ans = min(ans, x - lst[j][0])
        xpy[d[u]][x+y].append(i)
        for j in xpy[d['D']][x+y]:
            if lst[j][0] < x:
                ans = min(ans, (x - lst[j][0])*2)
        xmy[d[u]][x-y+20000].append(i)
        for j in xmy[d['U']][x-y+20000]:
            if lst[j][0] < x:
                ans = min(ans, (x-lst[j][0])*2)
# print(lst)
if ans == 1001001001:
    print("SAFE")
else:
    print(ans*5)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
