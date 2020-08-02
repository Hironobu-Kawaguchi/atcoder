# https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_b
# import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
ans = 'NO'
if (V-W)*T >= abs(B-A):
    ans = 'YES'
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
