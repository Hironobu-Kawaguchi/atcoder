# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_b

s = input()
n = len(s)
joi, ioi = 0, 0
for i in range(n-2):
    if s[i:i+3] == "JOI":
        joi += 1
    elif s[i:i+3] == "IOI":
        ioi += 1
print(joi)
print(ioi)
