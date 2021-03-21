# https://atcoder.jp/contests/abc168/tasks/abc168_b

# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

K = int(input())
S = input()
if len(S) <= K:
    print(S)
else:
    print(S[:K]+'...')


# N = int(input())
# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
