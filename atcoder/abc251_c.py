# https://atcoder.jp/contests/abc251/tasks/abc251_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S, T = [], []
st = set()
original = [False] * N
for i in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))
    if s not in st:
        original[i] = True
        st.add(s)
mxt = -1
ans = 0
for i in range(N):
    if original[i] and T[i]>mxt:
        ans = i+1
        mxt = T[i]
print(ans)


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
