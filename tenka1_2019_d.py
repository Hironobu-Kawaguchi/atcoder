# D - Three Colors
# https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_d
# 動的計画法(dynamic programming)
import math
import numpy as np
N = int(input())
a = np.array([int(input()) for _ in range(N)])
s = np.sum(a)
m = 998244353
dp1 = np.zeros((N+1, s+1), dtype=np.int64)
dp1[0, 0] = 1
dp2 = np.zeros((N+1, s//2+1), dtype=np.int64)
dp2[0, 0] = 1
for i, ai in enumerate(a):
    dp1[i+1, :]   += dp1[i, :] * 2 % m
    dp1[i+1, ai:] += dp1[i, :-ai]
    dp2[i+1, :]   += dp2[i, :] % m
    dp2[i+1, ai:] += dp2[i, :-ai]
subset1 = np.sum(dp1[N, math.ceil(s/2):])
subset2 = 0 if s % 2 == 1 else dp2[N, s//2]
print((3 ** N - 3 * subset1 + 3 * subset2) % m)

"""
import math
import numpy as np

N = int(input())
A = np.array([int(input()) for _ in range(N)])
S = np.sum(A)
MOD = 998244353

# dp0[i][j]: number of ways to obtain sum j for one of colors using first i integers.
# i = 0, 1, ..., N
# j = 0, 1, ..., S
dp0 = np.zeros((N + 1, S + 1), dtype=np.int64)

# dp1[i][j]: number of ways to obtain sum j for one of colors using first i integers,
#     but this time we use only TWO colors.
#     This will be used to find the number of cases when
#         (sum of R)= (sum of G) = S/2 & (sum of B) = 0 

dp1 = np.zeros((N + 1, S // 2 + 1), dtype=np.int64)

# using 0 integer to obtain sum=0
dp0[0, 0] = 1
dp1[0, 0] = 1

for i, x in enumerate(A):

    # If we do not use the next integer x, e.g. not for R, the sum of R is same, but possible ways are doubled
    #     because x can be used for either G or B
    dp0[i+1, :] += dp0[i, :] * 2 % MOD

    # Then we update the case when we use the next integer x.
    #     Lets say, sum=p was obtained for 4 different ways without using current integer x,
    #     then sum=p+x can also be obtained for 4 different ways.
    dp0[i+1, x:] += dp0[i, :-x]

    # If we do not use the next integer x, e.g. not for R, the sum of R is same, and possible ways are the same
    #     because this time we use only TWO colors. (say R and G, we dont use x for R, then automatically x goes for G)
    dp1[i+1, :] += dp1[i, :] % MOD

    # Then we update the case when we use the next integer x.
    dp1[i+1, x:] += dp1[i, :-x]


# count cases: (R >= S / 2)
not_satisfy = np.sum(dp0[N][math.ceil(S/2):])

# count cases: (R = S / 2) & (B = S / 2)
double_reduct = 0 if S % 2 == 1 else dp1[N][S/2]

# total cases = 3 ** N

ans = (3 ** N - 3 * not_satisfy + 3 * double_reduct) % MOD
print(ans)
"""