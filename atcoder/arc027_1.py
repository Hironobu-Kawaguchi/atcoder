# https://atcoder.jp/contests/arc027/tasks/arc027_1

h, m = map(int, input().split())
ans = 18*60 - (h*60 + m)
print(ans)
