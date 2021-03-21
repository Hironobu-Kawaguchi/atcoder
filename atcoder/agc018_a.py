# https://atcoder.jp/contests/agc018/tasks/agc018_a

from fractions import gcd
N, K = map(int, input().split())
A = list(map(int, input().split()))

g = A[0]
mx = A[0]
for i in range(N-1):
    g = gcd(g, A[i+1])
    mx = max(mx, A[i+1])

if K%g == 0 and K <= mx:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
