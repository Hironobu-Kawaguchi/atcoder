# https://atcoder.jp/contests/apc001/tasks/apc001_b

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dif = sum(b) - sum(a)

numa, numb = 0, 0
for i in range(n):
    if a[i] > b[i]:
        numb += a[i] - b[i]
    elif a[i] < b[i]:
        numa += (b[i] - a[i] + 1) // 2

# if numa <= dif and numb <= dif:
if numa <= dif:
    print('Yes')
else:
    print('No')
