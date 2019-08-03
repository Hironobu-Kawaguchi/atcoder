# https://atcoder.jp/contests/abc002/tasks/abc002_2

W = input()
ans = ''

for w in W:
    if w in ['a', 'i', 'u', 'e', 'o']:
        continue
    else:
        ans += w
print(ans)
