# https://atcoder.jp/contests/arc038/tasks/arc038_a

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans = 0
for i in range(0, N, 2):
    ans += A[i]
print(ans)
