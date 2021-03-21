# https://atcoder.jp/contests/abc137/tasks/abc137_a

A, B = map(int, input().split())

ans = max(max(A+B, A-B), A*B)
print(ans)
