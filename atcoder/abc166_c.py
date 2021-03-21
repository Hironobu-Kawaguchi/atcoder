# https://atcoder.jp/contests/abc166/tasks/abc166_b
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
H = list(map(int, (input().split())))
ans = [1] * N
for i in range(M):
    A, B = map(int, input().split())
    if H[A-1] <= H[B-1]:
        ans[A-1] = 0
    if H[B-1] <= H[A-1]:
        ans[B-1] = 0
print(sum(ans))


# S = input()
# A = [[int(i) for i in input().split()] for _ in range(N)]