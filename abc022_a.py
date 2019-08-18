# https://atcoder.jp/contests/abc022/tasks/abc022_a

N, S, T = map(int, input().split())
W = int(input())
A = [0]
for i in range(N-1):
    A.append(int(input()))

ans = 0
for i in range(N):
    W += A[i]
    if W >= S and W <= T:
        ans += 1

print(ans)

