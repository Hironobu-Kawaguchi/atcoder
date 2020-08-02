# https://atcoder.jp/contests/abc060/tasks/abc060_b

A, B, C = map(int, input().split())
ans = "NO"
for i in range(B):
    if A * i % B == C:
        ans = "YES"
        break
print(ans)