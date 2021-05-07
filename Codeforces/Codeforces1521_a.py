# https://codeforces.com/contest/1521/problem/A

from math import gcd

def main():
    A, B = map(int, input().split())
    # if A%B==0:
    if B==1:
        print("NO")
        return
    x = A * (B + 1)
    z = A * B * 2
    y = z - x
    print("YES")
    print(x, y, z)
    assert x%A==0
    assert x%(A*B)!=0
    assert y%A==0
    assert y%(A*B)!=0
    assert z%(A*B)==0
    assert y>=1
    return

t = int (input())
for _ in range(t):
    main()
