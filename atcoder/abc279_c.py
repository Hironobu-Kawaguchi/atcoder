# https://atcoder.jp/contests/ABC279/tasks/abc279_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]
st, tt = [], []
for j in range(W):
    stmp, ttmp = '', ''
    for i in range(H):
        stmp += S[i][j]
        ttmp += T[i][j]
    st.append(stmp)
    tt.append(ttmp)
st.sort()
tt.sort()
# print(st)
# print(tt)
if st==tt:
    print("Yes")
else:
    print("No")



# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
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
