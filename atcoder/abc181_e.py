# https://atcoder.jp/contests/abc181/tasks/abc181_e
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()

from bisect import bisect_left
N, M = map(int, input().split())
H = list(map(int, (input().split())))
H.sort()
W = list(map(int, (input().split())))
W.sort()

H_diff =[]
H_odd_cum, H_even_cum = [0], [0]
for i in range(N-1):
    H_diff.append(H[i+1]-H[i])
    if i%2:
        H_odd_cum.append(H_odd_cum[-1]+H_diff[-1])
    else:
        H_even_cum.append(H_even_cum[-1]+H_diff[-1])

ans = 1001001001001001
for i in range(0,N,2):   # 奇数番目だけ見れば良い
    if H[i] <= W[0]:
        tmp = W[0] - H[i]
    elif H[i] >= W[-1]:
        tmp = H[i] - W[-1]
    else:
        tmp = min(W[bisect_left(W, H[i])]-H[i], H[i]-W[bisect_left(W, H[i])-1])
    if i==0:
        tmp += H_odd_cum[-1]
    elif i==N-1:
        tmp += H_even_cum[-1]
    else:
        tmp += H_even_cum[i//2]
        tmp += H_odd_cum[-1] - H_odd_cum[i//2]
    ans = min(ans, tmp)
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
