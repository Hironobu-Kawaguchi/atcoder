# https://atcoder.jp/contests/arc117/tasks/arc117_a

A, B = map(int, input().split())
ans = [0]*(A+B)
if A>B:
    for i in range(A):
        ans[i] = i+1
        ans[A+B-1] -= i+1
    for i in range(B-1):
        ans[A+i] = -(i+1)
        ans[A+B-1] += i+1
else:
    for i in range(A-1):
        ans[i] = i+1
        ans[A-1] -= i+1
    for i in range(B):
        ans[A+i] = -(i+1)
        ans[A-1] += i+1
print(*ans)

