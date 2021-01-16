# https://atcoder.jp/contests/keyence2021/tasks/keyence2021_c

MOD = 998244353
h, w, k = map(int, input().split())
# g = [['.']*w for _ in range(h)]
d = dict()
for i in range(k):
    _h, _w, c = input().split()
    d[(int(_h)-1, int(_w)-1)] = c
# print(g)
dp = [[0]*w for _ in range(h)]
dp[0][0] = pow(3, h*w-k, MOD)
# dp[0][0] = 1
powinv3 = pow(3, MOD-2, MOD)

for i in range(h):
    for j in range(w):
        if i<h-1:
            # if (i,j) not in d:   dp[i+1][j] += dp[i][j] * 2 // 3
            if (i,j) not in d:   dp[i+1][j] += dp[i][j] * 2 * powinv3
            elif d[(i,j)]!='R': dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= MOD
        if j<w-1:
            # if (i,j) not in d:   dp[i][j+1] += dp[i][j] * 2 // 3
            if (i,j) not in d:   dp[i][j+1] += dp[i][j] * 2 * powinv3
            elif d[(i,j)]!='D': dp[i][j+1] += dp[i][j]
            dp[i][j+1] %= MOD

# print(dp)
# print(dp[h-1][w-1] * pow(3, h*w-k, MOD))
print(dp[h-1][w-1])



# h, w, k = map(int, input().split())
# g = [['.']*w for _ in range(h)]
# for i in range(k):
#     _h, _w, c = input().split()
#     g[int(_h)-1][int(_w)-1] = c
# print(g)
# dp_sum = [[0]*w for _ in range(h)]

# for c1 in ['R', 'D', 'X']:
#     for c2 in ['R', 'D', 'X']:
#         for c3 in ['R', 'D', 'X']:
#             dp = [[0]*w for _ in range(h)]
#             dp[0][0] = 1
#             g[0][0] = c1
#             g[1][1] = c2
#             g[2][1] = c3
#             for i in range(h):
#                 for j in range(w):
#                     if i<h-1 and g[i][j]!='R': dp[i+1][j] += dp[i][j]
#                     if j<w-1 and g[i][j]!='D': dp[i][j+1] += dp[i][j]
#             print(c1, c2, c3, dp)
#             for i in range(h):
#                 for j in range(w):
#                     dp_sum[i][j] += dp[i][j]

# print(dp_sum)
