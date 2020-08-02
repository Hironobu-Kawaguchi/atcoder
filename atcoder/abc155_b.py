# https://atcoder.jp/contests/abc155/tasks/abc155_b

N = int(input())
A = list(map(int, input().split()))

ans = 'APPROVED'
for i in range(N):
    if (A[i]%2 == 0) and (A[i]%3 != 0) and (A[i]%5 != 0):
        ans = 'DENIED'
        break

print(ans)
