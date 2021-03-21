# https://atcoder.jp/contests/abc148/tasks/abc148_e

N = int(input())

ans = N // 10

tmp = N // 10
while 5 <= tmp:
    ans += tmp // 5
    tmp = tmp // 5

if N % 2:
    print(0)
else:
    print(ans)
