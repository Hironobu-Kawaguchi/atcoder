# https://atcoder.jp/contests/abc167/tasks/abc167_b

# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

A, B, C, K = map(int, input().split())
ans = min(A,K) - max(0, K-A-B)
print(ans)


# N = int(input())
# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
