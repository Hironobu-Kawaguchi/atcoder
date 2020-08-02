# https://codeforces.com/contest/1236/problem/A

n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    y = min(b, c//2)
    b -= y
    x = min(a, b//2)
    print((x+y)*3)
