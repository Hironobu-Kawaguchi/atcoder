# https://atcoder.jp/contests/arc154/tasks/arc154_c
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)


def main():
    N = int(input())
    A = list(map(int, (input().split())))
    B = list(map(int, (input().split())))
    BC = []
    for i in range(N):
        if len(BC)==0:
            BC.append(B[i])
        elif B[i]!=BC[-1]:
            BC.append(B[i])
    if len(BC)>1 and BC[-1]==BC[0]:
        BC.pop()

    def check(start):
        if len(BC)==N and A!=BC:    # N種類あったらずらせない
            return False
        pos_a = 0
        pos_b = start
        while pos_a<len(A) and pos_b<len(BC)+start:
            if A[pos_a]==BC[pos_b%len(BC)]:
                pos_b += 1
            pos_a += 1
            if pos_b==len(BC)+start:
                return True
        # print(A, BC, pos_a, pos_b, file=sys.stderr)
        return False

    for i in range(len(BC)):
        if check(i):
            print("Yes")
            return
    print("No")
    return

T = int(input())
for _ in range(T):
    main()


# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# import sys
# it = map(int, sys.stdin.buffer.read().split())
# N = next(it)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
