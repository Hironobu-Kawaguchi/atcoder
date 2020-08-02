# https://atcoder.jp/contests/abc156/tasks/abc156_f

import sys
input = sys.stdin.buffer.readline

k, q = map(int, (input().split()))
d = list(map(int, (input().split())))

for qi in range(q):
    n, x, m = map(int, input().split())
    last = x
    eq = 0
    for i in range(k):
        num = ((n-1-i)+(k-1))//k
        last += (d[i]%m) * num
        if d[i]%m == 0: eq += num
    ans = (n-1) - (last//m - x//m) - eq
    print(ans)


# TLE
# import fractions
# import sys
# input = sys.stdin.buffer.readline

# k, q = map(int, (input().split()))
# d = list(map(int, (input().split())))
# sumd = sum(d)

# for i in range(q):
#     n, x, m = map(int, input().split())
#     lcm = sumd * m // fractions.gcd(sumd, m)
#     ans = 0
#     a = [x]
#     for i in range(n-1):
#         j = i%k
#         a.append(a[-1] + d[j])
#         if (a[-2] % m) < (a[-1] % m):
#             ans += 1
#     print(ans)
