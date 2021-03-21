# https://atcoder.jp/contests/abc094/tasks/abc094_b

N, M, X = map(int, input().split())
A = list(map(int, input().split()))

left, right = 0, 0
for i in range(M):
    if A[i] < X:
        left += 1
    if A[i] > X:
        right += 1

ans = min(left, right)
print(ans)
