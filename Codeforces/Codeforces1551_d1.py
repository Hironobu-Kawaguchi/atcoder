# http://codeforces.com/contest/1551/problem/D1


def main():
    n, m, k = map(int, input().split())
    if n%2:
        if k<m//2:
            print("NO")
            return
        else:
            k -= m//2
            n -= 1
    if m%2:
        if (n*m//2)-k<n//2:
            print("NO")
            return
        else:
            m -= 1
    if n%2==0 and m%2==0:
        if k%2==0:
            print("YES")
        else:
            print("NO")
    return

t = int(input())
for i in range(t):
    main()
