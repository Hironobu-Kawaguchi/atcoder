# https://atcoder.jp/contests/abc081/tasks/arc086_a

N, K = map(int, input().split())
A = list(map(int, input().split()))

l = [0] * (N+1)
for i in range(N):
    l[A[i]] += 1
l.sort(reverse=True)
ans = N - sum(l[:K])
print(ans)
