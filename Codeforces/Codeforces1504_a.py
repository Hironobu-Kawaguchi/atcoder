# https://codeforces.com/contest/1504/problem/A

t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    if s.count('a')==n:
        print('NO')
    else:
        print('YES')
        for i, c in enumerate(s):
            if c!='a':
                if i*2<=n:
                    j = n-i
                else:
                    j = n-i-1
                ans = s[:j] + 'a' + s[j:]
                break
        print(ans)

