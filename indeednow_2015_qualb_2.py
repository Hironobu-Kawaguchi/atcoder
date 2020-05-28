# https://atcoder.jp/contests/indeednow-qualb/tasks/indeednow_2015_qualb_2

s = input()
t = input()
n = len(s)
s += s
ans = -1
for i in range(n):
    if s[n-i:2*n-i] == t:
        ans = i
        break
print(ans)
