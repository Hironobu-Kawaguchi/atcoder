# https://atcoder.jp/contests/abc138/tasks/abc138_b

N = int(input())
A = list(map(int, input().split()))

bunbo = 0.0
for i in range(N):
    bunbo += 1/A[i]
ans = 1/bunbo
print(ans)
