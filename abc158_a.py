# https://atcoder.jp/contests/abc158/tasks/abc158_a

import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

S = input()
n = int(input())
N, K = map(int, input().split())
l = list(map(int, (input().split())))
A = [[int(i) for i in input().split()] for _ in range(N)]

N = int(input())
ans = (N+1) // 2
print(ans)
