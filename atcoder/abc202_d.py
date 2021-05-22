# https://atcoder.jp/contests/abc202/tasks/abc202_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

A, B, K = map(int, input().split())
dp = [[[0]*2 for _ in range(B+1)] for _ in range(A+1)]
for a in range(A+1):
    dp[a][0][0] = 1
for b in range(B+1):
    dp[0][b][1] = 1
for a in range(1, A+1):
    for b in range(1, B+1):
        dp[a][b][0] = dp[a-1][b][0] + dp[a][b-1][0]
        dp[a][b][1] = dp[a-1][b][1] + dp[a][b-1][1]

# for a in range(A+1):
#     for b in range(B+1):
#         print(a, b, dp[a][b])

ans = ''
while K>0:
    # print(A, B, K, ans)
    if K > dp[A][B][0]:
        K -= dp[A][B][0]
        B -= 1
        if B<0: break
        ans += 'b'
    else:
        A -= 1
        if A<0: break
        ans += 'a'
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
