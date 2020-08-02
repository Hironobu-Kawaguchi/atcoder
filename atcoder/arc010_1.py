# https://atcoder.jp/contests/arc010/tasks/arc010_1

N, M, A, B = map(int, input().split())
c = [int(input()) for _ in range(M)]

ans = "complete"
for i in range(M):
    if N <= A:
        N += B
    N -= c[i]
    if N < 0:
        ans = i+1
        break

print(ans)
