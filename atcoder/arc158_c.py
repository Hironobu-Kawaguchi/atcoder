# https://atcoder.jp/contests/arc158/tasks/arc158_c
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
import bisect

def main():
    N = int(input())
    A = list(map(int, (input().split())))

    def f(x):
        ret = 0
        while x:
            ret += x % 10
            x //= 10
        return ret

    # ans = 0
    # for i in range(N):
    #     for j in range(N):
    #         ans += f(A[i] + A[j])
    # print(ans)

    ans = 0
    for i in range(N):
        ans += f(A[i]) * N * 2
    # print(ans)
    # 繰り上がりの回数x9を引く
    cnt = 0
    for k in range(15):
        B = []
        for i in range(N):
            B.append(A[i]%(10**(k+1)))
        B.sort()
        for i in range(N):
            cnt += N - bisect.bisect_left(B, 10**(k+1) - B[i])
    # print(cnt)
    ans -= cnt * 9
    print(ans)
    return

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
