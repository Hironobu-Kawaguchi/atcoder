# https://atcoder.jp/contests/abc149/tasks/abc149_b

A, B, K = map(int, input().split())
if A >= K:
    A -= K
else:
    B = max(B+A-K, 0)
    A = 0
print(A, B)
