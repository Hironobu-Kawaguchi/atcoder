# https://atcoder.jp/contests/abc203/tasks/abc203_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

abc = list(map(int, (input().split())))
dice = [0]*7
for i in range(3):
    dice[abc[i]] += 1
flg = 0
ans = 0
for i in range(1,7):
    if dice[i]==3:
        flg = 3
        ans = i
        break
    elif dice[i] == 2:
        flg = 2
if flg == 2:
    for i in range(1,7):
        if dice[i]==1:
            ans = i
            break
print(ans)


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
