# https://atcoder.jp/contests/abc070/tasks/abc070_b

A, B, C, D = map(int, input().split())
ans = max(min(B, D) - max(A, C), 0)
print(ans)
