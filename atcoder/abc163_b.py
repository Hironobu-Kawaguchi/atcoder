# https://atcoder.jp/contests/abc163/tasks/abc163_b

N, M = map(int, input().split())
A = list(map(int, (input().split())))
sumA = sum(A)
if N>=sumA:
    print(N - sumA)
else:
    print(-1)


# S = input()
# N = input()
# A = [[int(i) for i in input().split()] for _ in range(N)]