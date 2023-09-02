# https://atcoder.jp/contests/arc154/tasks/arc154_b
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = list(input())
T = list(input())

if sorted(S)!=sorted(T):
    print(-1)
    exit()

ans = N
now = N-1
for i in range(N-1, -1, -1):
    while now>=0 and S[i]!=T[now]:
        now -= 1
    if now<0: break
    ans -= 1
    now -= 1
    print(ans, i, S[i], now, T[now], file=sys.stderr)
print(ans)

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
