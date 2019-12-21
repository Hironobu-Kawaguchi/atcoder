# https://atcoder.jp/contests/arc098/tasks/arc098_b

N = int(input())
A, S = [0] * (N+1), [0] * (N+1)
a = list(map(int, input().split()))
for i in range(N):
    A[i+1] = A[i] ^ a[i]
    S[i+1] = S[i] + a[i]
ans = 0
l = 1
for r in range(1, N+1):
    while (S[r]-S[l-1]) != (A[r]^A[l-1]):
        l += 1
    ans += r-l+1
print(ans)
