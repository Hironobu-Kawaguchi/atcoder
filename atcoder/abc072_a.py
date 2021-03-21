# https://atcoder.jp/contests/abc072/tasks/abc072_a

X, t = map(int, input().split())
ans = max(X -t, 0)
print(ans)