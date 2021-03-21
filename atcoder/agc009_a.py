# https://atcoder.jp/contests/agc009/tasks/agc009_a

N = int(input())
A, B = [0] * N, [0] * N
for i in range(N):
    a, b = map(int, input().split())
    A[i], B[i] = a, b
A.reverse()
B.reverse()

ans = 0
for i in range(N):
    mod = (A[i]+ans) % B[i]
    if mod:
        ans += B[i] - mod

print(ans)
