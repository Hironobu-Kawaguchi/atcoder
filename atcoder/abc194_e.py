# https://atcoder.jp/contests/abc194/tasks/abc194_e

N, M = map(int, input().split())
A = list(map(int, (input().split())))
pre = [-1] * N
ans = N
for i in range(N):
    if i-pre[A[i]]>M:
        ans = min(ans, A[i])
    pre[A[i]] = i
for i in range(N):
    if N-pre[i]>M:
        ans = min(ans, i)
print(ans)
