# https://atcoder.jp/contests/abc160/tasks/abc160_a
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

S = input()
if S[2]==S[3] and S[4]==S[5]:
    print("Yes")
else:
    print("No")

# N, M = map(int, input().split())
# n = int(input())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
