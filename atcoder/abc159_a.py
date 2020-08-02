# https://atcoder.jp/contests/abc159/tasks/abc159_a
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
ans = (N+M)*(N+M-1)//2 - N*M
print(ans)

# S = input()
# n = int(input())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
