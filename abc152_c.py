# https://atcoder.jp/contests/abc152/tasks/abc152_c

N = int(input())
P = list(map(int, input().split()))
mn = N+1
ans = 0
for i in range(N):
    if P[i] < mn:
        ans += 1
    mn = min(mn, P[i])
print(ans)
