# https://atcoder.jp/contests/abc152/tasks/abc152_d

from collections import defaultdict

def f(x):
    a = x%10
    b = 0
    while x:
        b = x
        x //= 10
    return (a,b)

N = int(input())
freq = defaultdict(int)
for i in range(N):
    p = f(i+1)
    freq[p] += 1
ans = 0
for i in range(N):
    p = f(i+1)
    q = (p[1], p[0])
    ans += freq[q]
print(ans)
