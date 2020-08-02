# https://atcoder.jp/contests/agc013/tasks/agc013_a

N = int(input())
A = list(map(int, input().split()))

ans = 1
up, dn = False, False
for i in range(N-1):
    if A[i] < A[i+1]:
        up = True
    elif A[i] > A[i+1]:
        dn = True
    if up and dn:
        ans += 1
        up, dn = False, False
print(ans)
