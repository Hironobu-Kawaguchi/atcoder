# https://atcoder.jp/contests/abc094/tasks/arc095_a

N = int(input())
X = list(map(int, input().split()))
A = sorted(X)

leftB = A[N//2 - 1]
rightB = A[N//2]

for i in range(N):
    if X[i] <= leftB:
        print(rightB)
    else:
        print(leftB)
