# https://atcoder.jp/contests/past201912/tasks/past201912_d

N = int(input())
A = [int(input()) for _ in range(N)]

cnt = [0] * N
for i in range(N):
    cnt[A[i]-1] += 1

x, y = 0, 0
for i in range(N):
    if cnt[i] == 0:
        x = i+1
    elif cnt[i] == 2:
        y = i+1

if x == 0:
    print("Correct")
else:
    print(y, x)
