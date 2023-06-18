# https://atcoder.jp/contests/arc158/tasks/arc158_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
import bisect
from itertools import permutations
INF = 1001001001.0

def main():
    N = int(input())
    x = list(map(int, (input().split())))
    x.sort()
    st = set([0,1, N-2, N-1])
    zero_idx = bisect.bisect_left(x, 0)
    for i in range(2):
        if zero_idx - 1 - i<0: break
        st.add(zero_idx - 1 - i)
    for i in range(2):
        if zero_idx + i>N-1: break
        st.add(zero_idx + i)
    # print(st)
    mx = -INF
    mn = INF
    for i in range(N):
        for j, k in permutations(st, 2):
            if i==j or i==k: continue
            # print(i, j, k)
            tmp = (x[i]+x[j]+x[k])/(x[i]*x[j]*x[k])
            mx = max(mx, tmp)
            mn = min(mn, tmp)
    print(mn)
    print(mx)
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
