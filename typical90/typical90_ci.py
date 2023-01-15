# https://atcoder.jp/contests/typical90/tasks/typical90_ci

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import copy
INF = 10**9 + 1

def main():
    N, P, K = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(N)]

    changeable = []
    for i in range(N):
        for j in range(i+1, N):
            if A[i][j]==-1:
                changeable.append((i,j))
    # print(len(changeable), changeable)

    def wf(x):
        B = copy.deepcopy(A)
        for i, j in changeable:
            B[i][j] = x
            B[j][i] = x
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    B[i][j] = min(B[i][j], B[i][k] + B[k][j])
        return B

    def count_ok(x):
        cnt = 0
        B = wf(x)
        for i in range(N):
            for j in range(i+1, N):
                if B[i][j]<=P:
                    cnt += 1
        # print(x, cnt, B)
        return cnt

    if count_ok(1)<K:
        print(0)
        return

    l, r = 0, INF
    while l+1<r:
        now = (l+r)//2
        if count_ok(now)<K+1:
            r = now
        else:
            l = now
    # print(l, r, count_ok(l), count_ok(r))
    min_x = r

    l, r = 0, INF
    while l+1<r:
        now = (l+r)//2
        if count_ok(now)<K:
            r = now
        else:
            l = now
    # print(l, r, count_ok(l), count_ok(r))
    max_x = l
 
    if r==INF and min_x!=INF:
        print("Infinity")
        return
    ans = max_x - min_x + 1
    print(ans)
    return

main()