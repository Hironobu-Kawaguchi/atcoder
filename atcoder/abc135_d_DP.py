# https://atcoder.jp/contests/abc135/tasks/abc135_d
# https://atcoder.jp/contests/abc135/submissions/6584488

S = input()

N = 13
# dp[k] -> 13で割った余りがKのパターン数
dp = [0] * N
dp[0] = 1

# 後ろから解くアルゴリズム
# 1?2?3   0 -> 3 -> ?3 -> 2?3 -> ...
mod = 10**9 + 7

mul = 1
for i in range(len(S))[::-1]:
    # 次の状態
    nextDP = [0] * N
    if S[i] == '?':
        for k in range(10):
            for j in range(N):
                nextDP[(k * mul + j) % N] += dp[j]
                nextDP[(k * mul + j) % N] %= mod
    else:
        k = int(S[i])
        for j in range(N):
            nextDP[(k * mul + j) % N] += dp[j]
            nextDP[(k * mul + j) % N] %= mod
    mul *= 10
    mul %= N
    dp = nextDP

print(dp[5])



# import numpy as np
# import math
# import itertools
# # S = input()
# mod = 10**9 + 7

# for S in itertools.product(['?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], repeat=4):
#     ans = 0
#     # n = np.zeros(len(S), dtype=int)
#     n = []
#     chk = []
#     for i in range(len(S)):
#         if S[i] == '?':
#             chk.append(i)
#             n.append('0')
#         else:
#             # n[i] = int(S[i])
#             n.append(S[i])

#     if len(chk) == 0:
#         break
#     elif chk[0] == 0:
#         # uso = math.ceil((10**(len(chk))-6) / 13)
#         uso = math.ceil((10**(len(chk))-6) / 13)
#     else:
#         # uso = math.ceil((10**(len(chk))-1) / 13)
#         uso = math.ceil((10**(len(chk))-1) / 13)
#     amari = int(''.join(list(n))) % 13


#     sums = np.zeros([len(chk), 10], dtype=int) 
#     for a in itertools.product(range(10), repeat=len(chk)):
#         for i, j in enumerate(a):
#             n[chk[i]] = str(j)
#         # print(n)
#         num = int(''.join(list(n)))
#         if num % 13 == 5:
#             ans += 1
#             # print(num)
#             for i, j in enumerate(a):
#                 n[chk[i]] = str(j)
#                 sums[i, j] += 1

#     if ans > uso:
#         print(S, ans, uso, amari)

# # print(chk)
# # print(sums)
# # print(ans % mod)

# # print('uso:{}'.format(uso))
# # print(amari)