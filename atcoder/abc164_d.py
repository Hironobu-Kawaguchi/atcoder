# https://atcoder.jp/contests/abc164/tasks/abc164_d

import sys
def input(): return sys.stdin.readline().rstrip()

S = list(input())
n = len(S)

dp = [0] * 2019
dp[0] = 1
tmp = 0
ten = 1
for i in range(n):
    tmp += int(S[n-1-i]) * ten
    tmp %= 2019
    ten *= 10
    ten %= 2019
    dp[tmp%2019] += 1
# print(dp)

ans = 0
for i in dp:
    if i >= 2:
        ans += i*(i-1)//2
        # print(i, dp[i])
print(ans)


# # nums = list(map(int, list(input())))
# lst = []
# ans = 0
# for i in range(n-4):
#     for j in range(i+3, n):
#         if int(S[i:j+1])%2019: continue
#         ans += 1
#         lst.append((i+1,j+1))

# print(ans)
# print(lst)

