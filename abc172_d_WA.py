# https://atcoder.jp/contests/abc172/tasks/abc172_d

# import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# @njit(cache=True)


# def main():
#     # @lru_cache(None)
#     # def dfs():
#     #     return
#     A, B = map(int, input().split())
#     print(A*B)
#     return

# main()

n = int(input())
div = [0] * (n+1)
div[1] = 1
div[2] = 2
div[3] = 2
for i in range(4,n+1):
    j = 2
    while j*j <= i:
        if i % j == 0:
            div[i] = div[i//j] + 1
            break
        j += 1
    if div[i] == 0:
        div[i] = 2
print(div)
ans = 0
for i in range(1,n+1):
    ans += div[i] * i
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
