# https://atcoder.jp/contests/past201912/tasks/past201912_f

from string import ascii_uppercase

def up2low(s):
    res = ''
    for i in range(len(s)):
        if i == 0 or i == len(s)-1:
            res += s[i].lower()
        else:
            res += s[i]
    return res

def low2up(s):
    res = ''
    for i in range(len(s)):
        if i == 0 or i == len(s)-1:
            res += s[i].upper()
        else:
            res += s[i]
    return res

S = input()
ss = []
up = []
for i in range(len(S)):
    if S[i] in ascii_uppercase:
        up.append(i)
for i in range(len(up)//2):
    ss.append(up2low(S[up[i*2]:up[i*2+1]+1]))
ss.sort()
for i in range(len(ss)):
    ss[i] = low2up(ss[i])

ans = ''.join(ss)
print(ans)
