# https://atcoder.jp/contests/agc003/tasks/agc003_b

n = int(input())
ans = 0
sums = 0
for i in range(n):
    a = int(input())
    sums += a
    if a == 0:
        ans += sums // 2
        sums = 0
ans += sums // 2
print(ans)
