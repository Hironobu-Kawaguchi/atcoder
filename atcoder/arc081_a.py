# https://atcoder.jp/contests/abc071/tasks/arc081_a

N = int(input())
A = list(map(int, input().split()))
A.sort()

pre = 10**10
cnt = 0
l = [0] * 2
i = N-1
while cnt < 2 and i > 0:
    if A[i] == A[i-1]:
        l[cnt] = A[i]
        cnt += 1
        i -= 2
    else:
        i -= 1

ans = l[0] * l[1]
print(ans)
