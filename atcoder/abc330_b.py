# https://atcoder.jp/contests/abc330/tasks/abc330_b

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, L, R = map(int, input().split())
A = list(map(int, input().split()))

X = []

for i in range(N):
    if L <= A[i] <= R:
        X.append(A[i])
    elif abs(L - A[i]) < abs(R - A[i]):
        X.append(L)
    else:
        X.append(R)
print(*X)
