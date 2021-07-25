# https://atcoder.jp/contests/arc123/tasks/arc123_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

A1, A2, A3 = map(int, input().split())
x = A2 - A1
y = A3 - A2
diff = y - x
ans = 0
if diff<0:
    ans = -diff
elif diff>0:
    ans = (diff+1) // 2
    if diff%2: ans += 1
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
