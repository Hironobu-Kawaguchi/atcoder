# https://atcoder.jp/contests/abc154/tasks/abc154_e

S = input()
n = len(S)
K = int(input())
dp = [[[0]*2 for _ in range(K+1)] for _ in range(n+1)]
dp[0][0][0] = 1
for i in range(n):          # i:桁
    for j in range(K+1):    # j:非0の数
        for k in range(2):  # k:0->nと同じ数,1->nより小さい数
            nd = int(S[i])  #nd:nのi桁
            for d in range(10):
                ni, nj, nk = i+1, j, k
                if d != 0: nj += 1      # 非0の数が増える
                if nj > K: continue     # 非0の数がKを超えたら計算不要
                if k == 0:              # ここまでnと同じ場合
                    if d > nd: continue # nより大きくなるのでダメ
                    if d < nd: nk = 1   # nより小さくなるのでkは1に
                dp[ni][nj][nk] += dp[i][j][k]
ans = dp[n][K][0] + dp[n][K][1]
print(ans)
