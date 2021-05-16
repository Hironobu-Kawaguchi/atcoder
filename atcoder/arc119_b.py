# https://atcoder.jp/contests/arc119/tasks/arc119_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)


def main():
    N = int(input())
    S = input()
    T = input()
    p_s, p_t = [], []
    for i in range(N):
        if S[i]=='0':
            p_s.append(i)
        if T[i]=='0':
            p_t.append(i)
    if len(p_s)!=len(p_t):
        print(-1)
        return
    ans = 0
    for i in range(len(p_s)):
        if p_s[i]!=p_t[i]:
            ans += 1
    print(ans)
    return

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
