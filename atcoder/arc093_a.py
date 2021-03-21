# https://atcoder.jp/contests/abc092/tasks/arc093_a

N = int(input())
A = [0] + list(map(int, input().split())) + [0]
Sums = []
for i in range(N+1):
    Sums.append(abs(A[i+1] - A[i]))

ans = sum(Sums)
for i in range(N):
    diff = Sums[i] + Sums[i+1] - abs(A[i+2] - A[i]) 
    print(ans - diff)
