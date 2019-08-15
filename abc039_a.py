# https://atcoder.jp/contests/abc039/tasks/abc039_a

A, B, C = map(int, input().split())
ans = (A*B + B*C + C*A) * 2
print(ans)
