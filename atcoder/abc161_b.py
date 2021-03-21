# https://atcoder.jp/contests/abc161/tasks/abc161_b
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
A = list(map(int, (input().split())))

sumA = sum(A)
cnt = 0
for i in range(N):
    if A[i]*4*M >= sumA:
        cnt += 1

if cnt >= M:
    print('Yes')
else:
    print('No')



# S = input()
# n = int(input())
# A = [[int(i) for i in input().split()] for _ in range(N)]
