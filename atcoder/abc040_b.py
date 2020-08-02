# https://atcoder.jp/contests/abc040/tasks/abc040_b

n = int(input())

ans = n
for x in range(1, int(n**0.5)+2):
    y, mod = divmod(n, x)
    ans = min(ans, abs(y-x) + mod)
print(ans)
