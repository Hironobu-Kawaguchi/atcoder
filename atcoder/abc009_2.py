# https://atcoder.jp/contests/abc009/tasks/abc009_2

N = int(input())

mx = 0
ans = 0

for i in range(N):
    a = int(input())
    if a > mx:
        ans = mx
        mx = a
    elif a > ans and a != mx:
        ans = a

print(ans)
