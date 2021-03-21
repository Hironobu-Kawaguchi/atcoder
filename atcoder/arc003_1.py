# https://atcoder.jp/contests/arc003/tasks/arc003_1

N = int(input())
r = input()

d = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
sumr = 0
for i in range(N):
    sumr += d[r[i]]
print(sumr / N)
