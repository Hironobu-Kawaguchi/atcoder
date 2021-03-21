# https://atcoder.jp/contests/abc155/tasks/abc155_e

S = input()
dp = [0, 1]
for s in S:
    i = int(s)
    a = min(dp[0] + i,   dp[1] + 10 - i)
    b = min(dp[0] + i+1, dp[1] + 10 - (i+1))
    dp = [a, b]
    # print(dp)
print(dp[0])


# WA
# # import os
# # import sys
# # input = sys.stdin.buffer.readline
# # S = input().rstrip().decode()
# S = input()
# n = len(S)
# ans = 0
# prej = 9
# se5 = 0
# for i in range(n):
#     j = int(S[i])
#     if prej == 5:
#         if j == 5:
#             se5 += 1
#         else:
#             ans -= se5
#             se5 = 0
#     prej = j
#     ans += min(j, 10-j)
# if prej == 5:
#     ans -= se5

# s0, s1 = int(S[0]), int(S[1])
# if s1 >= 6:
#     ans += 1
# elif s1 <=4 and s0 >= 5:
#     ans += 1
# print(ans)
