# https://codeforces.com/contest/1542/problem/C
# https://codeforces.com/blog/entry/92492

import math
MOD = 10**9+7

def lcm(a,b):
    return a*b//math.gcd(a,b)

def main():
    n = int(input())
    ans = n
    i = 1
    g = 1
    while g<=n and i<=n:
        g = lcm(g, i)
        ans += n//g
        i += 1
    ans %= MOD
    print(ans)
    return

t = int(input())
for _ in range(t):
    main()




# MAX_N = 10**16
# primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

# now = 1
# for p in primes:
#     now *= p
#     if now>MAX_N: break
# print(p, now)

# f = [0] * (MAX_N+5)
# for i in range(1, MAX_N+1):
#     for x in range(1, MAX_N+2):
#         if i%x!=0:
#             f[i] = x
#             break
# for i in range(1000):
#     print(i+1, f[i+1])

# for i in range(1, MAX_N+1):
#     f[i] += f[i-1]
#     f[i] %= MOD

# WA
# def main():
#     n = int(input())
#     ans = 0
#     for p in primes:
#         ans += ((n+p-1)//p)*p
#         ans %= MOD
#         n -= (n+p-1)//p
#     print(ans)
#     return

# t = int(input())
# for _ in range(t):
#     main()

