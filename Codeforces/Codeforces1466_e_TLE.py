# https://codeforces.com/contest/1466/problem/E
MOD = 10**9+7
P = 60  # 2**60まで

def main():
    n = int(input())
    x = list(map(int, input().split()))
    cnt = [0]*P  # 2進数で合算 sum(f(x,c))
    for i in range(n):
        for j in range(P):
            cnt[j] += (x[i] >> j) & 1
    ans = 0
    for i in range(n):
        exp_or, exp_and = 0, 0
        for j in range(P):
            if (x[i] >> j) & 1:  # f(xj,c)==1
                exp_or += (1 << j) % MOD * n
                exp_and += (1 << j) % MOD * cnt[j]
            else:              # f(xj,c)==0
                exp_or += (1 << j) % MOD * cnt[j]
        exp_or %= MOD
        exp_and %= MOD
        ans += (exp_and * exp_or) % MOD
        ans %= MOD
    print(ans)
    return

t = int(input())
for i in range(t):
    main()


# TLE 解法
# MOD = 10**9+7

# def main():
#     n = int(input())
#     x = list(map(int, input().split()))
#     ans = 0
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 ans += (x[i]&x[j]) * (x[j]|x[k])
#                 ans %= MOD
#     print(ans)
#     return

# t = int(input())
# for i in range(t):
#     main()
