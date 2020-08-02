# https://atcoder.jp/contests/abc037/tasks/abc037_a

A, B, C = map(int, input().split())
ans = max(C//A, C//B)
print(ans)
