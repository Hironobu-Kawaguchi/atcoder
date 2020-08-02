# https://codeforces.com/contest/1263/problem/C

t = int(input())
for i in range(t):
    ans = 0
    n = int(input())
    s = set([0])
    ans = [0]
    i = n
    while i > 0:
        tmp = n // i
        if tmp not in s:
            s.add(tmp)
            ans.append(tmp)
        i = min(n//(tmp+1), i-1)
    print(len(ans))
    print(*ans)
