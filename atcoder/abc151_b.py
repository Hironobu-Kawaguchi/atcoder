# https://atcoder.jp/contests/abc151/tasks/abc151_b

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

ans = N * M
for i in range(N-1):
    ans -= A[i]

ans = max(ans, 0)

if ans <= K:
    print(ans)
else:
    print(-1)
