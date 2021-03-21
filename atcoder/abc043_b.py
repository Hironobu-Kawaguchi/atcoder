# https://atcoder.jp/contests/abc043/tasks/abc043_b

s = input()
ans = ''
for i in range(len(s)):
    if s[i] == 'B':
        ans = ans[:-1]
    else:
        ans += s[i]
print(ans)
