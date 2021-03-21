# https://atcoder.jp/contests/arc009/tasks/arc009_1

N = int(input())
ans = 0
for i in range(N):
    a, b = map(int, input().split())
    ans += a*b
ans = int(ans*1.05)
print(ans)
