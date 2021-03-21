# https://atcoder.jp/contests/abc147/tasks/abc147_a

A = list(map(int, input().split()))
sm = sum(A)
if sm >= 22:
    print("bust")
else:
    print("win")
