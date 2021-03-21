# https://atcoder.jp/contests/abc098/tasks/abc098_a

A, B = map(int, input().split())
ans = max(max(A+B, A-B), A*B)
print(ans)
