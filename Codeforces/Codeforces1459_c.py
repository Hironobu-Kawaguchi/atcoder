# https://codeforces.com/contest/1459/problem/C

from math import gcd
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = []
if n==1:
    for j in range(m):
        ans.append(a[0]+b[j])
else:
    for i in range(n-1):
        if i==0:
            max_gcd = abs(a[i+1] - a[i])
        else:
            max_gcd = gcd(max_gcd, abs(a[i+1] - a[i]))
    for j in range(m):
        ans.append(gcd(max_gcd, a[0]+b[j]))
print(*ans)



# TLE
# from math import gcd
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# ans = []
# for j in range(m):
#     for i in range(n):
#         if i==0:
#             res = a[i]+b[j]
#         else:
#             res = gcd(res, a[i]+b[j])
#     ans.append(res)
# print(*ans)
