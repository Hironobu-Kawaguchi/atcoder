# https://atcoder.jp/contests/abc221/tasks/abc221_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
# MOD = 998244353

S = list(input())
T = list(input())

ans = "No"
if S==T: ans = "Yes"
for i in range(len(S)-1):
    S[i], S[i+1] = S[i+1], S[i]
    if S==T: ans = "Yes"
    S[i], S[i+1] = S[i+1], S[i]

print(ans)


# S = input()
# T = input()

# def main():
#     ans = 'Yes'
#     if S==T:
#         print(ans)
#         return
#     chk = []
#     for i in range(len(S)):
#         if S[i]!=T[i]:
#             chk.append(i)
#     if len(chk)==2 and chk[0]+1==chk[1] and S[chk[0]]==T[chk[1]] and S[chk[1]]==T[chk[0]]:
#         print(ans)
#     else:
#         print('No')
#     return

# main()

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
