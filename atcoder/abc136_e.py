# https://atcoder.jp/contests/abc136/tasks/abc136_e

N, K = map(int, input().split())
A = list(map(int, input().split()))
sumA = sum(A)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort(reverse=True)
    return divisors

divs = make_divisors(sumA)

for i in divs:
    mod = []
    for j in range(N):
        mod.append(A[j] % i)
    mod.sort(reverse=True)
    tmp = sum(mod) // i # -する数
    tmp = tmp * i - sum(mod[:tmp])  # -する合計数
    if tmp <= K:
        ans = i
        break

print(ans)
