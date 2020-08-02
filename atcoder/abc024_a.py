# https://atcoder.jp/contests/abc024/tasks/abc024_a

A, B, C, K = map(int, input().split())
S, T = map(int, input().split())
ans = A * S + B * T
if S + T >= K:
    ans -= C * (S + T)
print(ans)
