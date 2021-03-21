# https://atcoder.jp/contests/abc131/tasks/abc131_c

import fractions
A, B, C, D = map(int, input().split())

CD = (C * D) // fractions.gcd(C, D)

ans = B - A + 1
ans -= B//C - (A-1)//C
ans -= B//D - (A-1)//D
ans += B//CD - (A-1)//CD

print(ans)
