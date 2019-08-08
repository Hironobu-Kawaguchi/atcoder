# https://atcoder.jp/contests/abc069/tasks/arc080_a

N = int(input())
a = list(map(int, input().split()))

n1, n2, n4 = 0, 0, 0
for i in range(N):
    if a[i] % 2:
        n1 += 1
    elif a[i] % 4:
        n2 += 1
    else:
        n4 += 1

if n2 == 0:
    if n1 <= n4 + 1:
        print('Yes')
    else:
        print('No')
else:
    if n1 <= n4:
        print('Yes')
    else:
        print('No')
