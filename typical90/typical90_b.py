# https://atcoder.jp/contests/typical90/tasks/typical90_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def check(s):
    now = 0
    for c in s:
        if c=='(': now += 1
        else:      now -= 1
        if now<0:
            return False
    if now==0:
        return True
    return False

N = int(input())
ans = []
for i in range(1<<N):
    tmp = ''
    for j in range(N):
        if (i>>j)&1: tmp += '('
        else:        tmp += ')'
    if check(tmp):
        ans.append(tmp)
ans.sort()
for s in ans:
    print(s)


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
