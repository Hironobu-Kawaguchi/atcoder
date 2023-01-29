# https://atcoder.jp/contests/abc287/tasks/abc287_e
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = [(input(), i) for i in range(N)]
# print(S)
S.sort()

def lcp(s, t):
    ret = 0
    for i in range(min(len(s), len(t))):
        if s[i]==t[i]:
            ret += 1
        else:
            break
    return ret

ans = [0] * N
for i in range(N):
    if i>0:
        ans[S[i][1]] = max(ans[S[i][1]], lcp(S[i][0], S[i-1][0]))
    if i<N-1:
        ans[S[i][1]] = max(ans[S[i][1]], lcp(S[i][0], S[i+1][0]))
for i in range(N):
    print(ans[i])


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
