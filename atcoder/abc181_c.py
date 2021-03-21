# https://atcoder.jp/contests/abc181/tasks/abc181_c
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
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

def check(a, b):
    if a[0] == 0:
        if b[0] == 0:
            return True
        else:
            return False
    if b[0] == 0:
        if a[0] == 0:
            return True
        else:
            return False
    if a[1] == 0:
        if b[1] == 0:
            return True
        else:
            return False
    if b[1] == 0:
        if a[1] == 0:
            return True
        else:
            return False    
    if (a[0]*b[1] == a[1]*b[0]):
        return True
    return False

from itertools import combinations
N = int(input())
ans = "No"
xy = []
for i in range(N):
    x, y = map(int, input().split())
    xy.append((x,y))
for a, b, c in combinations(range(N), 3):
    # print(a, b, c)
    if check((xy[a][0]-xy[b][0], xy[a][1]-xy[b][1]), (xy[a][0]-xy[c][0], xy[a][1]-xy[c][1])):
        ans = "Yes"
        # print(a, b, c)
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
