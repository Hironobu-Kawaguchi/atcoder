# https://atcoder.jp/contests/abc058/tasks/abc058_b

O = input()
E = input()

ans = ''
for i in range(len(E)):
    ans += O[i] + E[i]
if len(O) != len(E):
    ans += O[-1]

print(ans)
