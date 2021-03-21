# https://atcoder.jp/contests/abc134/tasks/abc134_d

N = int(input())
a = list(map(int, input().split()))

memo = [0] * N
for i in range(1, N+1)[::-1]:
    sm = sum([memo[j-1] for j in range(i, N+1, i)])
    memo[i-1] = (sm + a[i-1]) % 2

M = sum(memo)
print(M)

ans = []
for i in range(N):
    if memo[i] == 1:
        ans.append(i+1)
print(*ans)
