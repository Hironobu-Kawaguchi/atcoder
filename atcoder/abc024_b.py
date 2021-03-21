# https://atcoder.jp/contests/abc024/tasks/abc024_b

N, T = map(int, input().split())
A = [int(input()) for _ in range(N)]
ans = T
for i in range(N-1):
    ans += min(T, A[i+1] - A[i])
print(ans)
