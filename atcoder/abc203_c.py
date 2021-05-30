# https://atcoder.jp/contests/abc203/tasks/abc203_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])
AB.sort()
now = 0
for i in range(N):
    # print(now, K, AB[i][0], AB[i][1])
    if AB[i][0] - now > K:
        ans = now + K
        break
    else:
        K -= AB[i][0] - now
        K += AB[i][1]
        now = AB[i][0]
else:
    ans = now + K

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
