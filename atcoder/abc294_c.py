# https://atcoder.jp/contests/abc294/tasks/abc294_c

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
import bisect

def main():
    N, M = map(int, input().split())
    A = list(map(int, (input().split())))
    B = list(map(int, (input().split())))
    C = A + B
    C.sort()
    # print(C)

    def f(X):
        ans = []
        for x in X:
            idx = bisect.bisect_left(C, x)
            ans.append(idx + 1)
        print(*ans)
        return

    f(A)
    f(B)
    return

main()


    # S = input()
    # N = int(input())
    # N, K = map(int, input().split())
    # A = list(map(int, (input().split())))
    # A = [[int(i) for i in input().split()] for _ in range(N)]
