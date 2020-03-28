# https://atcoder.jp/contests/abc160/tasks/abc160_d
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

import heapq

X, Y, A, B, C = map(int, input().split())
p = list(map(lambda x:int(x)*(-1), (input().split())))
heapq.heapify(p)
q = list(map(lambda x:int(x)*(-1), (input().split())))
heapq.heapify(q)
r = list(map(lambda x:int(x)*(-1), (input().split())))
heapq.heapify(r)
# print(p)

ans = 0
while r and (X>0 or Y>0):
    if p and p[0] < r[0] and X>0:
        ans -= heapq.heappop(p)
        X -= 1
    elif q and q[0] < r[0] and Y>0:
        ans -= heapq.heappop(q)
        Y -= 1
    elif p and q and p[0] < q[0] and Y>0:
        ans -= heapq.heappop(r)
        Y -= 1
    elif X>0:
        ans -= heapq.heappop(r)
        X -= 1
    else:
        ans -= heapq.heappop(r)
        Y -= 1
if X>0:
    for i in range(X):
        ans -= heapq.heappop(p)
if Y>0:
    for i in range(Y):
        ans -= heapq.heappop(q)
print(ans)



# X = int(input())
# S = input()
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
