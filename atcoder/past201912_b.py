# https://atcoder.jp/contests/past201912/tasks/past201912_b

N = int(input())
A = [int(input()) for _ in range(N)]

for i in range(N-1):
    if A[i] == A[i+1]:
        print("stay")
    elif A[i] < A[i+1]:
        print("up", A[i+1]-A[i])
    else:
        print("down", A[i]-A[i+1])
