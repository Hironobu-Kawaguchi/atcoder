# https://atcoder.jp/contests/arc141/tasks/arc141_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def main():
    S = input()
    candidates = []
    for i in range(1, len(S)):
        if len(S)%i: continue
        candidate = S[:i] * (len(S)//i)
        if int(candidate)<=int(S): candidates.append(int(candidate))
        if int(S[:i])>=2 and len(S[:i])==len(str(int(S[:i])-1)):
            candidate = (str(int(S[:i])-1)) * (len(S)//i)
            if int(candidate)<=int(S): candidates.append(int(candidate))
    candidates.sort(reverse=True)
    # print(candidates)
    if len(candidates)==0:
        return '9'*(len(S)-1)
    return candidates[0]

T = int(input())
for ti in range(T):
    print(main())


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
