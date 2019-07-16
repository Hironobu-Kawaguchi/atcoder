# B - 1 Dimensional World's Tale
# https://atcoder.jp/contests/abc110/tasks/abc110_b

N, M, X, Y = map(int, input().split())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

if max(X, max(x)) < min(Y, min(y)):
    print("No War")
else:
    print("War")
