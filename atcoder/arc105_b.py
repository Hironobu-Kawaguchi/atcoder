# https://atcoder.jp/contests/arc105/tasks/arc105_b

from math import gcd

def main():
    n = int(input())
    a = list(map(int, (input().split())))
    ans = a[0]
    for x in a:
        ans = gcd(ans, x)
    print(ans)
    return
    
main()
