# https://atcoder.jp/contests/abc193/tasks/abc193_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)


K = int(input())
S = input()
T = input()
cards = [K]*10
s, t = [0]*10, [0]*10
for i in range(4):
    cards[int(S[i])] -= 1
    cards[int(T[i])] -= 1
    s[int(S[i])] += 1
    t[int(T[i])] += 1
win, denom = 0, 0

def f(num, lst):
    res = 0
    for i in range(1,10):
        if i==num:
            res += i * (10**lst[i]) * 10
        else:
            res += i * (10**lst[i])
    return res

for i in range(1,10):
    for j in range(1,10):
        if i==j:
            cnt = cards[i] * (cards[j] - 1)
        else:
            cnt = cards[i] * cards[j]
        denom += cnt
        if f(i,s) > f(j,t):
            win += cnt
print(win/denom)

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
