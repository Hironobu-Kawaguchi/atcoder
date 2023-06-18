# https://atcoder.jp/contests/abc294/tasks/abc294_b

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

def main():
    H, W = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(H)]
    for i in range(H):
        s = ''
        for j in range(W):
            if A[i][j]==0:
                s += '.'
            else:
                s += chr(A[i][j]-1+ord('A'))
        print(s)
    return

main()


    # S = input()
    # N = int(input())
    # N, K = map(int, input().split())
    # A = list(map(int, (input().split())))
    # A = [[int(i) for i in input().split()] for _ in range(N)]
