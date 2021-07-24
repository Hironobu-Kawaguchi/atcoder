# http://codeforces.com/contest/1553/problem/B


def main():
    s = input().rstrip()
    t = input().rstrip()
    ans = "NO"
    for i in range(len(s)):
        if s[i]!=t[0]: continue
        for r in range(len(t)+1):
            if len(s)-i<r: continue
            l = len(t)-r
            if i+r-l-1<0: continue
            tmp = s[i:i+r] + s[i+r-l-1:i+r-1][::-1]
            # print(i, r, l, tmp)
            if tmp==t:
                ans = "YES"
                break
    print(ans)
    return

q = int(input())
for i in range(q):
    main()
