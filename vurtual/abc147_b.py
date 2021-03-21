# https://atcoder.jp/contests/abc147/tasks/abc147_a
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

S = input()
n = len(S)//2
ans = 0
for i in range(n):
    if S[i] != S[-1-i]:
        ans += 1
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
