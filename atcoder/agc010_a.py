# https://atcoder.jp/contests/agc010/tasks/agc010_a

N = int(input())
A = list(map(int, input().split()))
sm = 0
for i in range(N):
    sm += A[i]%2
if sm%2:
    print("NO")
else:
    print("YES")
