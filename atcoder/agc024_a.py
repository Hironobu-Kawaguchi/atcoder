# https://atcoder.jp/contests/agc024/tasks/agc024_a

A, B, C, K = map(int, input().split())

if K % 2:
    print(B-A)
else:
    print(A-B)
