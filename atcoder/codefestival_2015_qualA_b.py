# https://atcoder.jp/contests/code-festival-2015-quala/tasks/codefestival_2015_qualA_b

n = int(input())
a = list(map(int,input().split()))
ans = 0
cnt = 1
for i in range(n):
    ans += a[n-1-i] * cnt
    cnt *= 2
print(ans)
