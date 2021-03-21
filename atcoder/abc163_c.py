# https://atcoder.jp/contests/abc163/tasks/abc163_c

N = int(input())
A = list(map(int, (input().split())))
ans = [0] * N

for i in range(N-1):
    ans[A[i]-1] += 1
for i in range(N):
    print(ans[i])


# S = input()
# N, M = map(int, input().split())
# A = [[int(i) for i in input().split()] for _ in range(N)]