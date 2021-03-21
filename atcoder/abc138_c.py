# https://atcoder.jp/contests/abc138/tasks/abc138_c

N = int(input())
v = list(map(int, input().split()))
v.sort()

ans = 0.0 + v[0]
for i in range(1, N):
    ans = (ans + v[i]) / 2
print(ans)
