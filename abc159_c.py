# https://atcoder.jp/contests/abc159/tasks/abc159_c
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

L = int(input())
ans = L*L*L/(3*3*3)
print(ans)

# S = input()

# N, M = map(int, input().split())
# ans = (N+M)*(N+M-1)//2 - N*M
# print(ans)

# n = int(input())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
