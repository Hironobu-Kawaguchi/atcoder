# A - Buttons
# https://atcoder.jp/contests/abc124/tasks/abc124_a

A, B = map(int, input().split())
if A == B:
    print(A*2)
else:
    print(max(A, B)*2 -1)