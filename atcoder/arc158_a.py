# 
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
import time

def main():
    # start_time =time.time()
    # print(start_time)
    x = list(map(int, (input().split())))
    x.sort()
    # print(x[0], x[1], x[2])

    if x[0]%2!=x[1]%2 or x[0]%2!=x[2]%2:
        print(-1)
        return

    def f(x):
        return (x[2]*2-x[1]-x[0])

    if f(x)%6:
        print(-1)
        return

    ans = 0
    while f(x):
        tmp = f(x) // 6
        a = (x[2] + x[1] - x[0] * 2) // 6
        c = 0
        if a>tmp: c = a - tmp
        x[0] += a * 4 + (tmp-a+c) * 2
        x[1] += (tmp-a+c) * 4 + (a-c) * 2
        x[2] += c * 2
        ans += tmp + c
        # print(ans, tmp, a, c, x)
        x.sort()
        # print(time.time() - start_time)
        # if time.time() - start_time > 1e-5:
        #     ans = -1
        #     break
    print(ans)
    return

T = int(input())
for ti in range(T):
    main()


# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
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
