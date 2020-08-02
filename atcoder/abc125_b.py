# B - Resale
# https://atcoder.jp/contests/abc125/tasks/abc125_b

N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
for i in range(N):
    temp = V[i] - C[i]
    if temp > 0:
        ans += temp
print(ans)