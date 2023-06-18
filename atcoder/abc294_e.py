# https://atcoder.jp/contests/abc294/tasks/abc294_e

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
import bisect

def main():
    L, N1, N2 = map(int, input().split())
    v1, l1 = [], []
    for i in range(N1):
        v, l = map(int, input().split())
        v1.append(v), l1.append(l)
    cum1 = [0]
    for i in range(N1):
        cum1.append(cum1[-1] + l1[i])
    # print(cum1)
    v2, l2 = [], []
    for i in range(N2):
        v, l = map(int, input().split())
        v2.append(v), l2.append(l)
    cum2 = [0]
    for i in range(N2):
        cum2.append(cum2[-1] + l2[i])
    # print(cum2)
    cum = sorted(list(set(cum1) | set(cum2)))
    # print(cum)
    v1c = []
    for c in cum:
        # print(bisect.bisect_left(cum1, c))
        v1c.append(v1[bisect.bisect_left(cum1, c) - 1])
    v2c = []
    for c in cum:
        # print(bisect.bisect_left(cum2, c))
        v2c.append(v2[bisect.bisect_left(cum2, c) - 1])
    # print(v1c)
    # print(v2c)
    ans = 0
    for i in range(1, len(cum)):
        if v1c[i]==v2c[i]:
            ans += cum[i] - cum[i-1]
    print(ans)
    return

main()


    # S = input()
    # N = int(input())
    # N, K = map(int, input().split())
    # A = list(map(int, (input().split())))
    # A = [[int(i) for i in input().split()] for _ in range(N)]
