# https://atcoder.jp/contests/abc196/tasks/abc196_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

H, W, A, B = map(int, input().split())
used = [[False]*16 for _ in range(16)]

def dfs(i, j, a, b):
    global used
    if (a<0 or b<0): return 0
    if (j==W):
        j = 0
        i += 1
    if (i==H): return 1
    if used[i][j]: return dfs(i, j+1, a, b)        
    res = 0
    used[i][j] = True
    res += dfs(i, j+1, a, b-1)
    if (j<W-1 and not used[i][j+1]):
        used[i][j+1] = True
        res += dfs(i, j+1, a-1, b)
        used[i][j+1] = False
    if (i<H-1 and not used[i+1][j]):
        used[i+1][j] = True        
        res += dfs(i, j+1, a-1, b)
        used[i+1][j] = False
    used[i][j] = False
    return res

print(dfs(0,0, A, B))


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
