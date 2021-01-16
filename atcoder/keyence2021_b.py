# https://atcoder.jp/contests/keyence2021/tasks/keyence2021_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
a = list(map(int, (input().split())))

cnt = [0] * 300005
for y in a:
    cnt[y] += 1
for i in range(1, len(cnt)):
    cnt[i] = min(cnt[i], cnt[i-1])
# print(cnt)
ans = 0
for i in range(len(cnt)-1, 0, -1):
    dif = cnt[i-1] - cnt[i]
    if dif==0: continue
    add = min(k, dif)
    ans += add * i
    k -= add
    if k==0: break
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
