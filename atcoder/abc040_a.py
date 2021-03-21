# https://atcoder.jp/contests/abc040/tasks/abc040_a

n, x = map(int, input().split())
ans = min(x-1, n-x)
print(ans)
