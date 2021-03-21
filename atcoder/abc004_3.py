# https://atcoder.jp/contests/abc004/tasks/abc004_3

N = int(input())
N %= 30

l = ['1', '2', '3', '4', '5', '6']

for i in range(N):
    j1 = i % 5
    s1 = l[j1]
    j2 = i % 5 + 1
    s2 = l[j2]
    l[j1] = s2
    l[j2] = s1

print(''.join(l))
