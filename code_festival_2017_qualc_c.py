# https://atcoder.jp/contests/code-festival-2017-qualc/tasks/code_festival_2017_qualc_c

s = input()
l = 0
r = len(s)-1
ans = 0
while r-l > 0:
    if s[l] == s[r]:
        l += 1
        r -= 1
    elif s[l] == 'x':
        ans += 1
        l += 1
    elif s[r] == 'x':
        ans += 1
        r -= 1
    else:
        ans = -1
        break
print(ans)
