# https://codeforces.com/contest/1504/problem/D

# 12121
# 21212
# 12121
# 21212
# 12121

n = int(input())

n2 = n // 2
n1 = n - n2

sum2 = (n*n) // 2
sum1 = (n*n) - sum2

num1, num2 = 0, 0
while (num1<sum1 and num2<sum2):
    a = int(input())
    if a!=1:
        q, mod = divmod(num1, n)
        i = q * 2 + mod // n1
        j = (mod % n1) * 2 + (mod // n1)
        num1 += 1
        print(1, i+1, j+1, flush=True)
    else:
        q, mod = divmod(num2, n)
        i = q * 2 + mod // n2
        j = (mod % n2) * 2 + 1 - (mod // n2)
        num2 += 1
        print(2, i+1, j+1, flush=True)

if (num1<sum1):
    while (num1<sum1):
        a = int(input())
        q, mod = divmod(num1, n)
        i = q * 2 + mod // n1
        j = (mod % n1) * 2 + (mod // n1)
        num1 += 1
        if a!=1:
            print(1, i+1, j+1, flush=True)
        else:
            print(3, i+1, j+1, flush=True)
else:
    while (num2<sum2):
        a = int(input())
        q, mod = divmod(num2, n)
        i = q * 2 + mod // n2
        j = (mod % n2) * 2 + 1 - (mod // n2)
        num2 += 1
        if a!=2:
            print(2, i+1, j+1, flush=True)
        else:
            print(3, i+1, j+1, flush=True)
