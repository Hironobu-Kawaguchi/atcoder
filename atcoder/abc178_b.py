# https://atcoder.jp/contests/abc177/tasks/abc178_b

a, b, c, d = map(int, input().split())
if a<=0 and b>=0:
    xlist = [a,0,b]
else:
    xlist = [a,b]
if c<=0 and d>=0:
    ylist = [c,0,d]
else:
    ylist = [c,d]

ans = -1001001001001001001
for x in xlist:
    for y in ylist:
        ans = max(ans, x*y)
print(ans)