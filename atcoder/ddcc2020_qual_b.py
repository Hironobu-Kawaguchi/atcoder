# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_b

N = int(input())
A = list(map(int, input().split()))

left = 0
right = sum(A)
ans = 202020202020 * 200000

for i in range(N-1):
    tmp = A[i]
    left += tmp
    right -= tmp
    ans = min(ans, abs(right - left))

print(ans)

