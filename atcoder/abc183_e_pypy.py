# https://atcoder.jp/contests/abc183/tasks/abc183_f

# DP + 累積和
MOD = 10**9+7
H, W = map(int, input().split())
S = [input() for _ in range(H)]
dp = [[0]*W for _ in range(H)]
dp[0][0]=1
x = [[0]*W for _ in range(H)]
y = [[0]*W for _ in range(H)]
z = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j]=='#': continue
        if i==0 and j==0: continue
        if j>0:
            x[i][j] = (x[i][j-1] + dp[i][j-1]) % MOD
        if i>0:
            y[i][j] = (y[i-1][j] + dp[i-1][j]) % MOD
        if i>0 and j>0:
            z[i][j] = (z[i-1][j-1] + dp[i-1][j-1]) % MOD
        dp[i][j] = (x[i][j] + y[i][j] + z[i][j]) % MOD
print(dp[H-1][W-1])



# # DP
# MOD = 10**9+7
# H, W = map(int, input().split())
# S = [input() for _ in range(H)]

# cum = [1]
# cumsum = 1
# for i in range(max(H,W)):
#     cum.append(cumsum)
#     cumsum *= 2


# dp = [[[0]*W for _ in range(H)] for _ in range(3)]
# for k in range(3):
#     dp[k][0][0] = 1
# done = [[[False]*W for _ in range(H)] for _ in range(3)]
# for i in range(H):
#     for j in range(W):
#         if S[i][j]=='#': continue
#         ii = i
#         jj = j
#         while S[ii][jj]=='.':
#             ii += 1
#             if ii>=H: break
#             if done[0][i][j]:
#                 tmp = dp[1][i][j] + dp[2][i][j]
#             else:
#                 tmp = dp[0][i][j] + dp[1][i][j] + dp[2][i][j]
#             if i==0 and j==0: tmp = 1
#             if tmp==0: break
#             dp[0][ii][jj] += tmp * pow(2,ii-i-1)
#             dp[0][ii][jj] %= MOD
#             done[0][ii][jj] = True

#         ii = i
#         jj = j
#         while S[ii][jj]=='.':
#             jj += 1
#             if jj>=W: break
#             if done[1][i][j]:
#                 tmp = dp[0][i][j] + dp[2][i][j]
#             else:
#                 tmp = dp[0][i][j] + dp[1][i][j] + dp[2][i][j]
#             if i==0 and j==0: tmp = 1
#             if tmp==0: break
#             dp[1][ii][jj] += tmp * pow(2,jj-j-1)
#             dp[1][ii][jj] %= MOD
#             done[1][ii][jj] = True

#         ii = i
#         jj = j
#         while S[ii][jj]=='.':
#             ii += 1
#             if ii>=H: break
#             jj += 1
#             if jj>=W: break
#             if done[2][i][j]:
#                 tmp = dp[0][i][j] + dp[1][i][j]
#             else:
#                 tmp = dp[0][i][j] + dp[1][i][j] + dp[2][i][j]
#             if i==0 and j==0: tmp = 1
#             if tmp==0: break
#             dp[2][ii][jj] += tmp * pow(2,ii-i-1)
#             dp[2][ii][jj] %= MOD
#             done[2][ii][jj] = True
# ans = 0
# for k in range(3):
#     ans += dp[k][H-1][W-1]
# ans %= MOD
# print(ans)



# MOD = 10**9+7
# H, W = map(int, input().split())
# S = [input() for _ in range(H)]
# dp = [[0]*W for _ in range(H)]
# dp[0][0]=1
# for i in range(H):
#     for j in range(W):
#         if S[i][j]=='#': continue
#         ii = i
#         jj = j
#         while S[ii][jj]=='.':
#             ii += 1
#             if ii>=H: break
#             dp[ii][jj] += dp[i][j]
#             dp[ii][jj] %= MOD
#         ii = i
#         jj = j
#         while S[ii][jj]=='.':
#             jj += 1
#             if jj>=W: break
#             dp[ii][jj] += dp[i][j]
#             dp[ii][jj] %= MOD
#         ii = i
#         jj = j
#         while S[ii][jj]=='.':
#             ii += 1
#             if ii>=H: break
#             jj += 1
#             if jj>=W: break
#             dp[ii][jj] += dp[i][j]
#             dp[ii][jj] %= MOD
# print(dp[H-1][W-1]%MOD)