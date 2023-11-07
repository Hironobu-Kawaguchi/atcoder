# https://atcoder.jp/contests/abc320/tasks/abc320_b
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

S = input()

def is_kaibun(s: str) -> bool:
    return s == s[::-1]

ans = 0
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        if is_kaibun(S[i:j]):
            ans = max(ans, j-i)
print(ans)

