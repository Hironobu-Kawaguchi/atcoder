# https://atcoder.jp/contests/abc166/tasks/abc166_e
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))
l = [0] * N
r = [0] * N
for i in range(N):
    if A[i] + i < N:
        l[A[i]+i] += 1
    if i - A[i] >= 0:
        r[i-A[i]] += 1
ans = 0
for i in range(N):
    ans += l[i]*r[i]
print(ans)

# S = input()
# N, M = map(int, input().split())
# A = [[int(i) for i in input().split()] for _ in range(N)]