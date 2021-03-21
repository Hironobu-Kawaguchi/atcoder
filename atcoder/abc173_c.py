# https://atcoder.jp/contests/abc173/tasks/abc173_c

# import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# @njit(cache=True)


# def main():
#     # @lru_cache(None)
#     # def dfs():
#     #     return
#     A, B = map(int, input().split())
#     print(A*B)
#     return

# main()

H, W, K = map(int, input().split())
c = [input() for _ in range(H)]
# print(c)
ans = 0
for bi in range(1<<H):
    for bj in range(1<<W):
        cnt = 0
        for i in range(H):
            if (bi>>i)&1: continue
            for j in range(W):
                if (bj>>j)&1: continue
                if c[i][j]=='#':
                    cnt += 1
        if cnt==K:
            ans += 1
print(ans)


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
