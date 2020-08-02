# https://codeforces.com/contest/1265/problem/A

def main():
    s = input()
    ans = ''
    for i in range(len(s)):
        if s[i] == '?':
            lr = []
            if i != 0:
                lr.append(s[i-1])
            if i != len(s)-1:
                lr.append(s[i+1])
            if len(ans) != 0:
                lr.append(ans[-1])
            for c in abc:
                if c not in lr:
                    ans += c
                    break
        else:
            if i == 0:
                if s[i] == s[i+1]:
                    return '-1'
                else:
                    ans += s[i]
            elif i == len(s)-1:
                if s[i] == s[i-1]:
                    return '-1'
                else:
                    ans += s[i]
            else:
                if s[i] == s[i-1] or s[i] == s[i+1]:
                    return '-1'
                else:
                    ans += s[i]
    return ans

abc = ['a', 'b', 'c']
t = int(input())
for i in range(t):
    print(main())
