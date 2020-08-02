# https://atcoder.jp/contests/abc043/tasks/arc059_a

N = int(input())
a = list(map(int, input().split()))

ans = 100100100
for i in range(-100, 101):
    tmp = 0
    for j in range(N):
        tmp += (a[j] - i) ** 2
    ans = min(ans, tmp)
print(ans)

