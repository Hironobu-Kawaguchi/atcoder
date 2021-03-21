# https://atcoder.jp/contests/abc160/tasks/abc160_a
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

X = int(input())
div, mod = divmod(X, 500)
ans = div * 1000 + (mod//5)*5
print(ans)

# S = input()
# N, M = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
