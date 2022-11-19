# https://atcoder.jp/contests/abc276/tasks/abc276_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import bisect

N = int(input())
P = list(map(int, (input().split())))

st = set()
idx = -1
for i in range(N-1, 0, -1):
    st.add(P[i])
    if P[i-1]>P[i]:
        idx = i
        lst = sorted(list(st))
        nxt = lst[bisect.bisect(lst, P[i-1])-1]
        st.add(P[i-1])
        P[i-1] = nxt
        st.remove(nxt)
        break
lst = sorted(list(st), reverse=True)
for i in range(idx, N):
    P[i] = lst[i-idx]
print(*P)


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
