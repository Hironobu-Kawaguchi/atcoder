# https://atcoder.jp/contests/abc055/tasks/abc055_b

N = int(input())
ans = 1
for i in range(1, N+1):
    ans = ans * i % 1000000007
print(ans)
