# https://atcoder.jp/contests/arc152/tasks/arc152_a

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)


def main():
    N, L = map(int, input().split())
    A = list(map(int, (input().split())))
    num1 = 0
    for i in range(N):
        if L>=A[i]+1:
            L -= A[i]+1
            num1 += 1
        elif L>=A[i]:
            L -= A[i]
        elif A[i]==2:
            print("No")
            return
        else:
            num1 -= 1
    print("Yes")
    return

main()

# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
