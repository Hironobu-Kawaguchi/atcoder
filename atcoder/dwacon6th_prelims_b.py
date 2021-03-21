# https://atcoder.jp/contests/dwacon6th-prelims/tasks/dwacon6th_prelims_b

MOD = 10**9+7

N = int(input())
x = list(map(int, input().split()))

ans = 0
mul = 0
for i in range(N-1):
    mul += pow(i+1, MOD-2, MOD)
    ans += (x[i+1] - x[i]) * mul % MOD
    ans %= MOD
for i in range(2, N):
    ans *= i
    ans %= MOD
print(ans)


# WA
# import numpy as np
# # import math
# import sys
# readline = sys.stdin.buffer.readline
# MOD = 10**9+7

# def factorial(n, MOD):
#     res = 1
#     for i in range(n):
#         res *= i+1
#         res %= MOD
#     return res

# N = int(readline())
# x = np.array(readline().split(), dtype=np.int64)
# # print(N, x)

# dif = x[1:] - x[:N-1]
# # print(dif)

# cnt = np.zeros(N-1, dtype=np.int64)
# # sm = math.factorial(N-1)
# sm = factorial(N-1, MOD)
# for i in range(N-1):
#     if i == 0:
#         cnt[i] = sm
#         tmp = sm
#     else:
#         tmp = tmp * i // (i+1)
#         # tmp = sm // (i+1)
#         cnt[i] = cnt[i-1] + tmp
# # print(cnt)

# sums = np.mod((dif * cnt), MOD)
# # print(sms)
# ans = 0
# for i in range(N-1):
#     ans += sums[i]
#     ans %= MOD
# print(ans)


# # RE
# # import numpy as np
# # import math
# # import sys
# # readline = sys.stdin.buffer.readline
# # MOD = 10**9+7

# # N = int(readline())
# # x = np.array(readline().split(), dtype=np.int64)
# # # print(N, x)

# # # dif = np.zeros((N-1,N-1), dtype=np.int64)
# # dif = np.fmax(x[1:].reshape(-1, N-1) - x[:N-1].reshape(N-1, -1), 0)
# # # print(dif)

# # cnt = np.zeros((N-1,N-1), dtype=np.int64)
# # for i in range(N-1):
# #     for j in range(i+1):
# #         if i == 0:
# #             cnt[N-2-i, N-2-j] = math.factorial(N-1)
# #         elif j == 1:
# #             cnt[N-2-i, N-2-j] = cnt[N-2-i+1, N-2-j+1] // (i+1)
# #         elif j == 0:
# #             cnt[N-2-i, N-2-j] = cnt[N-2-i+1, N-2-j] * i // (i+1)
# #         else:
# #             cnt[N-2-i, N-2-j] = cnt[N-2-i+1, N-2-j+1]
# # # print(cnt)

# # ans = np.mod((dif * cnt), MOD)
# # # print(ans)
# # ans = ans.sum() % MOD
# # print(ans)
