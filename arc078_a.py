# https://atcoder.jp/contests/abc067/tasks/arc078_a

N = int(input())
a = list(map(int, input().split()))

suma = sum(a)
sums = [0]
for i in range(N):
    sums.append(sums[-1] + a[i])

ans = 10**14
for i in range(1, N):
    ans = min(ans, abs(suma - sums[i] * 2))

print(ans)
