# D - equeue
# https://atcoder.jp/contests/abc128/tasks/abc128_d

N, K = map(int, input().split())
V = [int(v) for v in input().split()]

nk = min(N, K)  # NとKのmin（Vから取れる宝石の上限数）
ans = 0

for i in range(1, nk + 1):   # i:取る宝石の数
    for j in range(i + 1):   # j:左端から取る宝石の数
        tmp = V[:j] + V[N-i+j:] # 左からj個、右からi-j個取る
        tmp.sort()
        ngcnt = 0   # マイナスの数
        vsum = 0
        for t in tmp:
            if t < 0 and ngcnt < K-i:
                ngcnt += 1
                continue
            else:
                vsum += t
        ans = max(vsum, ans)

print(ans)
