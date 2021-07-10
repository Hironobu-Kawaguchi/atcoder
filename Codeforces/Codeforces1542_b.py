# https://codeforces.com/contest/1542/problem/B
# https://codeforces.com/blog/entry/92492

def main():
    n, a, b = map(int, input().split())
    if a==1:
        if (n-1)%b==0:
            print("Yes")
        else:
            print("No")
    else:
        t = 1
        ok = False
        while t<=n:
            if t%b==n%b:
                ok = True
                break
            t *= a
        if ok:
            print("Yes")
        else:
            print("No")
    return

t = int(input())
for _ in range(t):
    main()
