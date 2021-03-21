# https://atcoder.jp/contests/abc145/tasks/abc145_d
# https://atcoder.jp/contests/abc145/submissions/8469534

X, Y = map(int, input().split())

def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    nf = rf = 1
    for i in range(r):
        nf = nf * (n-i) % mod
        rf = rf * (i+1) % mod
    return nf * pow(rf, mod-2, mod) % mod

def main():
    if (X+Y) % 3 or X > 2*Y or Y > 2*X:
        print(0)
        return
    n = (X+Y) // 3
    r = Y - n
    print(combination(n, r))

main()



# MOD = 1000000007

# def power_func(a,b,p):
#   """a^b mod p を求める"""
#   if b==0: return 1
#   if b%2==0:
#     d=power_func(a,b//2,p)
#     return d*d %p
#   if b%2==1:
#     return (a*power_func(a,b-1,p ))%p

# def comb(n,k,p):
#   """power_funcを用いて(nCk) mod p を求める"""
#   from math import factorial
#   if n<0 or k<0 or n<k: return 0
#   if n==0 or k==0: return 1
#   a=factorial(n) %p
#   b=factorial(k) %p
#   c=factorial(n-k) %p
#   return (a*power_func(b,p-2,p)*power_func(c,p-2,p))%p

# def main():
#     X, Y = map(int, input().split())

#     if (X + Y) % 3 != 0 or max(X,Y) > min(X,Y):
#         print(0)
#         return
#     a = X // 3
#     b = Y // 3
#     # print(a, b)

#     ans = comb(a+b, a, MOD)

#     # ans = 1
#     # for i in range(max(a,b), a+b):
#     #     ans *= i+1
#     #     ans %= MOD

#     print(ans)

# main()
