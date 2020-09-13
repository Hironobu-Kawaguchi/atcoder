# https://atcoder.jp/contests/abc177/tasks/abc178_e

n = int(input())
xpy_max = -1001001001
xpy_min =  1001001001
xmy_max = -1001001001
xmy_min =  1001001001

for i in range(n):
    x, y = map(int, input().split())
    xpy_max = max(xpy_max, x+y)
    xpy_min = min(xpy_min, x+y)
    xmy_max = max(xmy_max, x-y)
    xmy_min = min(xmy_min, x-y)
ans = max(xpy_max - xpy_min, xmy_max - xmy_min)
print(ans)
