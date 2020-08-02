# https://atcoder.jp/contests/code-festival-2016-quala/tasks/codefestival_2016_qualA_b

N = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(N):
    if a[a[i]-1] == i+1:
        ans += 1
print(ans//2)
