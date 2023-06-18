# https://atcoder.jp/contests/abc296/tasks/abc296_d

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
INF = 1001001001001001001

def main():
    N, M = map(int, input().split())
    X = INF
    for a in range(1, N + 1):
        b = (M + a - 1) // a
        if b > N: continue
        X = min(X, a * b)
        if a > b: break
    if X==INF:
        print(-1)
    else:
        print(X)
    return

main()
