# https://atcoder.jp/contests/arc164/tasks/arc164_a
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
import math

cand = []
for i in range(38):
    cand.append(3**i-1)
cand.reverse()
print(cand, file=sys.stderr)

def main():
    N, K = map(int, input().split())
    # max_m = int(math.log(N, 3))
    # print(max_m)
    if N==K:
        print("Yes")
        return
    N -= K
    if N%2:
        print("No")
        return
    ans = "No"
    nm = 0
    for c in cand:
        nm += N//c
        N -= (N//c)*c
        if N==0:
            break
    if nm<=K:
        ans = "Yes"
    print(ans)
    return

T = int(input())
for _ in range(T):
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
