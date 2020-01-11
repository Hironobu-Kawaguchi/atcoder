# https://atcoder.jp/contests/abc150/tasks/abc150_d

def gcd(a,b):
    if b:
        return gcd(b,a%b)
    else:
        return a

def lcm(a,b):
    return a*b//gcd(a,b)

def f(x):
    res = 0
    while x%2==0:
        x //= 2
        res += 1
    return res

def main():
    import sys
    readline = sys.stdin.buffer.readline
    N, M = map(int, readline().split())
    a = list(map(int, readline().split()))
    for i in range(N):
        a[i] //= 2

    t = f(a[0])
    for i in range(N):
        if f(a[i]) == t:
            a[i] >>= t
        else:
            print(0)
            return
    M >>= t

    l = 1
    for i in range(N):
        l = lcm(l, a[i])
        if l > M:
            print(0)
            return

    M //= l
    ans = (M + 1) // 2
    print(ans)

main()

# WA
# import fractions
# import sys
# readline = sys.stdin.buffer.readline
# N, M = map(int, readline().split())
# a = list(map(int, readline().split()))
# # print(N, M, a)

# MOD = 10**9 + 7

# tmp = 1
# for x in a:
#     x //= 2
#     tmp2 = x // fractions.gcd(tmp, x)
#     M //= tmp2
#     tmp *= tmp2
#     tmp %= MOD

# ans = (M + 1) // 2
# print(ans)

