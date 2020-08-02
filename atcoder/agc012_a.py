# https://atcoder.jp/contests/agc012/tasks/agc012_a

N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

ans = 0
for i in range(N):
    ans += a[2*i+1]
print(ans)
