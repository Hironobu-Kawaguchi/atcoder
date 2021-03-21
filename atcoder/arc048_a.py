# https://atcoder.jp/contests/arc048/tasks/arc048_a

A, B = map(int, input().split())
if A*B > 0:
    ans = B - A
else:
    ans = B - A - 1
print(ans)
