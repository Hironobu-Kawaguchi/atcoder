# B - Algae
# https://atcoder.jp/contests/abc127/tasks/abc127_b

r, D, x2000 = map(int, input().split())

ans = x2000
for i in range(10):
    ans = r * ans - D
    print(ans)
