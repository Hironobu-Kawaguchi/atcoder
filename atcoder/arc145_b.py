# https://atcoder.jp/contests/arc145/tasks/arc145_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

def main():
    N, A, B = map(int, input().split())
    N = max(0, N - (A - 1))
    p, mod = divmod(N, A)
    # print(p, mod)
    ans = p * min(B, A) + min(mod, B)
    print(ans)

main()

# AC
# def main():
#     N, A, B = map(int, input().split())
#     if A>N:
#         ans = 0
#     elif A<=B:
#         ans = N - A + 1
#     else:
#         p, mod = divmod(N - (A - 1), A)
#         # print(p, mod)
#         ans = p * B + min(mod, B)
#     print(ans)

# main()

