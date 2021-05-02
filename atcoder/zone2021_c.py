# https://atcoder.jp/contests/zone2021/tasks/zone2021_c

n = int(input())
m = 5
a = [[int(i) for i in input().split()] for _ in range(n)]
ac, wa = 0, 1001001001
while ac+1<wa:
    wj = (ac+wa)//2
    s = set()
    for i in range(n):
        x = 0
        for j in range(m):
            if a[i][j]>=wj:
                x |= (1<<j)
        s.add(x)
    ok = False
    for i in s:
        for j in s:
            for k in s:
                if (i|j|k)==(1<<m)-1:
                    ok = True
    if ok:
        ac = wj
    else:
        wa = wj
print(ac)
