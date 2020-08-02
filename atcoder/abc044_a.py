# https://atcoder.jp/contests/abc044/tasks/abc044_a

N = int(input())
K = int(input())
X = int(input())
Y = int(input())

ans = min(N, K) * X + max(N-K, 0) * Y
print(ans)
