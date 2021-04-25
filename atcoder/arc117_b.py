# https://atcoder.jp/contests/arc117/tasks/arc117_b

MOD = 10**9+7
N = int(input())
A = list(map(int, input().split()))
A.append(0)
A.sort()
ans = 1
for i in range(N):
    ans *= A[i+1] - A[i] + 1
    ans %= MOD
print(ans)
