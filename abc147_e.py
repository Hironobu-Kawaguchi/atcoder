# https://atcoder.jp/contests/abc147/tasks/abc147_e

H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
B = [list(map(int, input().split())) for i in range(H)]
center = 80 * (H+W)
C = [[abs(A[i][j] - B[i][j]) for j in range(W)] for i in range(H)]

dp = [[0] * W for i in range(H)]
dp[0][0] = (1 << (center + C[0][0])) | (1 >> (center - C[0][0]))

for i in range(H):
    for j in range(W):
        if i:
            dp[i][j] |= dp[i-1][j] << C[i][j]
            dp[i][j] |= dp[i-1][j] >> C[i][j]
        if j:
            dp[i][j] |= dp[i][j-1] << C[i][j]
            dp[i][j] |= dp[i][j-1] >> C[i][j]

ans = center * 2
for i in range(center*2):
    if (dp[H-1][W-1] >> i) & 1:
        ans = min(ans, abs(i-center))

print(ans)


# # TLE
# H, W = map(int, input().split())
# A = []
# for i in range(H):
#     A.append(list(map(int, input().split())))
# B = []
# for i in range(H):
#     B.append(list(map(int, input().split())))

# dp = [[[0] * ((H+W)*80) for _ in range(W)] for _ in range(H)]
# dp[0][0][abs(A[0][0]-B[0][0])] = 1

# for i in range(H):
#     for j in range(W):
#         dif = abs(A[i][j] - B[i][j])
#         if i > 0:
#             for k in range((H+W)*80):
#                 if dp[i-1][j][k] == 1:
#                     dp[i][j][k+dif] = 1
#                     if k >= dif:
#                         dp[i][j][k-dif] = 1
#                     else:
#                         dp[i][j][dif-k] = 1
#         if j > 0:
#             for k in range((H+W)*80):
#                 if dp[i][j-1][k] == 1:
#                     dp[i][j][k+dif] = 1
#                     if k >= dif:
#                         dp[i][j][k-dif] = 1
#                     else:
#                         dp[i][j][dif-k] = 1

# for k in range(H*W*80):
#     if dp[H-1][W-1][k] == 1:
#         ans = k
#         break

# print(ans)
