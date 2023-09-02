# https://atcoder.jp/contests/arc146/tasks/arc146_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, M, K = map(int, input().split())
A = list(map(int, (input().split())))

ans = 0
for bi in range(32, -1, -1):
    # bitを上から立てられるかどうかを調べる
    A.sort(reverse=True)

    ok = True
    cost = 0
    for j in range(K):
        if not (A[j]>>bi)&1:
            next_cost = (1<<bi) - (A[j] & ((1<<bi)-1))
            if cost + next_cost <= M:
                cost += next_cost
            else:
                ok = False
    # M以内でbitを立てられた
    if ok:
        cand = [False] * len(A)
        for j in range(len(A)):
            if j<K:     # costをかけているので、K番目までは必ずTrue
                cand[j] = True
            elif (A[j]>>bi)&1:  # 最初からbitが立っているものは残す
                cand[j] = True
        new_A = []
        for j in range(len(A)):
            if cand[j]:
                new_A.append(A[j])
        A = new_A.copy()
        for j in range(len(A)):
            if not (A[j]>>bi)&1:    # costをかけて(1<<bi)にしたもの
                A[j] = (1<<bi)
        ans += (1<<bi)
        M -= cost
    # M以内でbitを立てられなかった
    else:
        for j in range(len(A)):
            A[j] &= ((1<<bi)-1)

print(ans)



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
