# https://atcoder.jp/contests/code-festival-2014-qualb/tasks/code_festival_qualB_b
import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

n,k = map(int,input().split())
a = [int(input()) for _ in range(n)]
now = 0
i=0
while now < k:
    now += a[i]
    i += 1
print(i)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
