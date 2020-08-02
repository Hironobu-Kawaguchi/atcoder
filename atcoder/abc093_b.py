# https://atcoder.jp/contests/abc093/tasks/abc093_b

A, B, K = map(int, input().split())

if K >= B-A+1:
    ans = list(range(A, B+1))
else:
    ans = list(range(A, A+K)) + list(range(max(A+K, B-K+1), B+1))

for a in ans:
    print(a)
