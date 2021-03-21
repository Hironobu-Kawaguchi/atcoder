# https://atcoder.jp/contests/abc060/tasks/abc060_a

A, B, C = input().split()
if A[-1] == B[0] and B[-1] == C[0]:
    print("YES")
else:
    print("NO")
    