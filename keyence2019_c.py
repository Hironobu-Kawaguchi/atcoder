# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_c

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dif = []
ans = 0
tmp = 0
dsm = 0
for i in range(N):
    dif.append(A[i] - B[i])
    dsm += A[i] - B[i]
    if A[i] < B[i]:
        ans += 1
        tmp += B[i] - A[i]

if dsm < 0:
    print(-1)
else:
    dif.sort(reverse=True)
    i = 0
    while tmp > 0:
        tmp -= dif[i]
        i += 1
        ans += 1
    print(ans)
