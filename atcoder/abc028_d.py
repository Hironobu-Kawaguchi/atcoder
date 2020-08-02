# D - 乱数生成
# https://atcoder.jp/contests/abc028/tasks/abc028_d

N, K = map(int, input().split())
ans = (((K-1) * (N-K) * 6 +
        # (K-1) * 3 + (N-K) * 3 + 1)
        (N-1) * 3 + 1)
       / (N**3))
print(ans)
