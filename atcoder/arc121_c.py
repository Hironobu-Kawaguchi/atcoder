# https://atcoder.jp/contests/arc121/tasks/arc121_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)


def main():
    N = int(input())
    p = list(map(int, (input().split())))
    now = 1
    ans = []
    while True:
        ok = True
        for i in range(N-1, -1, -1):
            if p[i]!=i+1:
                ok = False
                break
        if ok: break
        now = 1-now
        for i in range(now, N-1, 2):
            if p[i]>p[i+1]:
                ans.append(i+1)
                p[i], p[i+1] = p[i+1], p[i]
                break
        else:
            ans.append(i+1)
            p[i], p[i+1] = p[i+1], p[i]

    print(len(ans))
    print(*ans)
    return

T = int(input())
for ti in range(T):
    main()

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
