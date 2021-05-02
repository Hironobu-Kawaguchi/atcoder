# https://codeforces.com/contest/1515/problem/B

import math

def main():
    n = int(input())
    if (n%2):
        print("NO")
        return
    while n%2==0:
        n //= 2
    i = int(math.sqrt(n)+0.01)
    if i*i==n:
        print("YES")
        return
    print("NO")

t = int(input())
for _ in range(t):
    main()
