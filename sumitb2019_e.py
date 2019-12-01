# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_e

MOD = 1000000007

N = int(input())
A = list(map(int, input().split()))

cnt = [-1, -1, -1]
ans = 1
for a in A:
    num = 0
    i = -1
    for j in range(3):
        if a == cnt[j] + 1:
            num += 1
            i = j
    if num == 0:
        ans = 0
        break
    ans *= num
    ans %= MOD
    cnt[i] = a

print(ans)
