# https://atcoder.jp/contests/abc064/tasks/abc064_c

N = int(input())
a = list(map(int, input().split()))

rates = [400, 800, 1200, 1600, 2000, 2400, 2800, 3200]
l = [0] * 8
tmp = 0
for i in range(N):
    for j in range(8):
        if a[i] < rates[j]:
            l[j] = 1
            break
    else:
        tmp += 1

print(max(sum(l), 1), sum(l)+tmp)
