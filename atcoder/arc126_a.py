# https://atcoder.jp/contests/arc126/tasks/arc126_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def main():
    N2, N3, N4 = map(int, input().split())
    ans = 0
    # 3*2, 4*1
    tmp = min(N3//2, N4)
    N3 -= tmp*2
    N4 -= tmp
    ans += tmp
    # 2*2, 3*2
    tmp = min(N3//2, N2//2)
    N3 -= tmp*2
    N2 -= tmp*2
    ans += tmp
    # 4*2, 2*1
    tmp = min(N4//2, N2)
    N4 -= tmp*2
    N2 -= tmp
    ans += tmp
    # 4*1, 2*3
    tmp = min(N4, N2//3)
    N4 -= tmp
    N2 -= tmp*3
    ans += tmp
    # 2*5
    ans += N2//5
    print(ans)
    return


T = int(input())
for _ in range(T):
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
