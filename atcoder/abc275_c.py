# https://atcoder.jp/contests/abc275/tasks/abc275_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
# from itertools import product

S = [input() for _ in range(9)]
# print(S)

def ok(x, y):
    return 0<=x<9 and 0<=y<9 and S[x][y]=='#'

ans = 0
for x1 in range(9):
    for y1 in range(9):
        for dx in range(9):
            for dy in range(9):
                if dx==0 and dx==0: continue
                x2, y2 = x1 + dx, y1 + dy
                x3, y3 = x2 - dy, y2 + dx
                x4, y4 = x3 - dx, y3 - dy
                if ok(x1,y1) and ok(x2,y2) and ok(x3,y3) and ok(x4,y4):
                    # print((x1, y1), (x2,y2), (x3,y3), (x4,y4))
                    ans += 1
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
