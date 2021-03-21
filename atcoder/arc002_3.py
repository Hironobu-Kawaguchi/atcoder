# https://atcoder.jp/contests/arc002/tasks/arc002_3

n = int(input())
s = input()
c = ['A', 'B', 'X', 'Y']
r = [''] * 4
ans = 1005
for i in range(4**4):
    for k in range(4):
        r[k] = c[(i>>(k*2))&3]
    x = 0
    j = 0
    while j < n-1:
        if (s[j]==r[0] and s[j+1]==r[1]) or (s[j]==r[2] and s[j+1]==r[3]):
            x += 1
            j += 2
        else:
            x += 1
            j += 1
    if j == n-1:
        x += 1
    ans = min(ans, x)
print(ans)
