# https://atcoder.jp/contests/abc143/tasks/abc143_a

A, B = map(int, input().split())
ans = max(A - B*2, 0)
print(ans)
