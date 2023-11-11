# https://atcoder.jp/contests/abc323/tasks/abc323_b
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = [input() for _ in range(N)]
score = []
for i in range(N):
    score.append((S[i].count('o'), -i))
score.sort(reverse=True)
ans = [-i+1 for _, i in score]
print(*ans)
