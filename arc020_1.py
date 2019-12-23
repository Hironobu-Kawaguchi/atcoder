# https://atcoder.jp/contests/arc020/tasks/arc020_1

A, B = map(int, input().split())
A = abs(A)
B = abs(B)
if A == B:
    print("Draw")
elif A < B:
    print("Ant")
else:
    print("Bug")
