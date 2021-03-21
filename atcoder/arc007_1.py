# https://atcoder.jp/contests/arc007/tasks/arc007_1

X = input()
s = input()
ans = ''
for c in s:
    if c != X:
        ans += c
print(ans)
