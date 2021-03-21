# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_c

X = int(input())

mn = X // 105
mx = (X + 99) // 100
ans = 0
for i in range(mn, mx+1, 1):
    if X >= i * 100 and X <= i * 105:
        ans = 1
        break

print(ans)
