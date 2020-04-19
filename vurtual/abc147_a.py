# https://atcoder.jp/contests/abc147/tasks/abc147_a
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

A = list(map(int, (input().split())))
if sum(A) >= 22:
    print("bust")
else:
    print("win")

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
