# https://atcoder.jp/contests/abc066/tasks/arc077_a

n = int(input())
a = list(map(int, input().split()))

b = [0] * n
for i in range(n):
    if i % 2 == n % 2:
        j = (n+i)//2
    else:
        j = (n-i)//2
    b[j] = a[i]
print(*b)
