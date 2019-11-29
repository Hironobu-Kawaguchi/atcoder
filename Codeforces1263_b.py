# https://codeforces.com/contest/1263/problem/B

t = int(input())
for i in range(t):
    ans = 0
    n = int(input())
    lines = []
    s = set()
    for j in range(n):
        line = input()
        if line in s:
            ans += 1
            plus = 0
            while line in s:
                plus += 1
                keta = 3 - plus // 10
                chg = str((int(line[keta]) + 1) % 10)
                tmp = ''
                for k in range(4):
                    if k == keta:
                        tmp += chg
                    else:
                        tmp += line[k]
                line = tmp
        s.add(line)
        lines.append(line)
    print(ans)
    for line in lines:
        print(line)
