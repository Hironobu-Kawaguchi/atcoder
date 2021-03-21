# https://atcoder.jp/contests/abc144/tasks/abc144_a

A, B = map(int, input().split())
if A <= 9 and B <= 9:
    print(A*B)
else:
    print(-1)
    