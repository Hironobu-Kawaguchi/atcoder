# https://atcoder.jp/contests/abc052/tasks/arc067_a

MOD = 1000000007
N = int(input())
d = dict()

for i in range(2, N+1):
    tmp = i
    div = 2
    while tmp > 1:
        if tmp % div == 0:
            if div not in d:
                d[div] = 1
            else:
                d[div] = d[div] + 1
            tmp = tmp // div
        else:
            div += 1
ans = 1
for div in d:
    ans = ans * (d[div] + 1) % MOD

print(ans)
