# https://atcoder.jp/contests/abc160/tasks/abc160_c
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

K, N = map(int, input().split())
A = list(map(int, (input().split())))
A.append(K+A[0])

ans = K
for i in range(N):
    ans = min(ans, K-(A[i+1]-A[i]))

print(ans)

# X = int(input())
# S = input()
# A = [[int(i) for i in input().split()] for _ in range(N)]
