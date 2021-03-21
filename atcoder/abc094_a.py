# https://atcoder.jp/contests/abc094/tasks/abc094_a

A, B, X = map(int, input().split())

if X >= A and X <= A+B:
    print('YES')
else:
    print('NO')
