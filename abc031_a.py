# https://atcoder.jp/contests/abc031/tasks/abc031_a

A, D = map(int, input().split())
if A <= D:
    ans = (A+1) * D
else:
    ans = A * (D+1)
print(ans)
