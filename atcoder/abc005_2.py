# https://atcoder.jp/contests/abc005/tasks/abc005_2

N = int(input())

ans = 101

for i in range(N):
    t = int(input())
    ans = min(t, ans)

print(ans)
