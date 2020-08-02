# https://atcoder.jp/contests/abc166/tasks/abc166_b
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
sunuke = [0] * N
for i in range(K):
    d = int(input())
    A = list(map(int, (input().split())))
    for j in range(d):
        sunuke[A[j]-1] = 1
ans = N - sum(sunuke)
print(ans)


# S = input()
# A = [[int(i) for i in input().split()] for _ in range(N)]