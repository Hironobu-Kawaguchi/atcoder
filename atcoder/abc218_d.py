# https://atcoder.jp/contests/ABC218/tasks/abc218_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)


from itertools import combinations

N = int(input())
xy = dict()
for i in range(N):
    x, y = map(int, input().split())
    if x not in xy:
        xy[x] = set([y])
    else:
        xy[x].add(y)
# print(xy)    

ans = 0
for i, j in combinations(xy.keys(), 2):
    # print(i, j, xy[i]&xy[j])
    ss = xy[i]&xy[j]
    ans += len(ss)*(len(ss)-1)//2
print(ans)


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# import sys
# it = map(int, sys.stdin.buffer.read().split())
# N = next(it)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
