# https://atcoder.jp/contests/abc161/tasks/abc161_c
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
ans = min(N%K, K-N%K)
print(ans)


# S = input()
# n = int(input())
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
