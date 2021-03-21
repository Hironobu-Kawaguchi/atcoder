# https://atcoder.jp/contests/abc164/tasks/abc164_b

A, B, C, D = map(int, input().split())

takahashi = (C+B-1)//B
aoki      = (A+D-1)//D
if takahashi <= aoki:
    print('Yes')
else:
    print('No')
