# https://atcoder.jp/contests/abc019/tasks/abc019_2

s = input()
ans = ''
n = 1
pre = s[0]
for i in range(1, len(s)):
    if s[i] == pre:
        n += 1
    else:
        ans += pre + str(n)
        n = 1
        pre = s[i]
ans += pre + str(n)

print(ans)
