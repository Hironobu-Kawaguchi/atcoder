# https://atcoder.jp/contests/abc027/tasks/abc027_b

N = int(input())
a = list(map(int, input().split()))
suma = sum(a)
if suma % N:
    ans = -1
else:
    mean = suma // N
    ans = 0
    tmp = 0
    for i in range(N-1):
        tmp += a[i]
        if tmp != mean * (i+1):
            ans += 1
print(ans)
