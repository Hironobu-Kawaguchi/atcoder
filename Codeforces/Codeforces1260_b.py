# https://codeforces.com/contest/1260/problem/B

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if (a+b)%3:
        print("NO")
    elif a > 2*b or b > 2*a:
        print("NO")
    else:
        print("YES")
