# https://atcoder.jp/contests/arc142/tasks/arc142_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, K = input().split()
N = int(N)
if K[-1]=='0':
    print(0)
elif K[::-1]<K:
    print(0)
else:
    cand = set()
    for i in range(13):
        tmp = int(K+'0'*i)
        if tmp<=N:
            cand.add(tmp)
        tmp = int(K[::-1]+'0'*i)
        if tmp<=N:
            cand.add(tmp)
    # print(cand)
    print(len(cand))


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
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
