# https://atcoder.jp/contests/abc037/tasks/abc037_c

N, K = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += a[i] * min(i+1, min(N-i, min(K, N-K+1)))
print(ans)
