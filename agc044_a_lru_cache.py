# https://atcoder.jp/contests/agc044/tasks/agc044_a

from functools import lru_cache

def solve(N, A, B, C, D):
    @lru_cache(None)
    def f(N):
        if N == 0:
            return 0
        if N == 1:
            return D
        ret = D * N
        q, r = divmod(N, 2)
        if r == 0:
            ret = min(ret, f(q) + A)
        else:
            ret = min(ret, f(q) + A + D, f(q + 1) + A + D)
        q, r = divmod(N, 3)
        if r == 0:
            ret = min(ret, f(q) + B)
        else:
            ret = min(ret, f(q) + B + D*r, f(q + 1) + B + D*(3-r))
        q, r = divmod(N, 5)
        if r == 0:
            ret = min(ret, f(q) + C)
        else:
            ret = min(ret, f(q) + C + D*r, f(q + 1) + C + D*(5-r))
        return ret

    return f(N)

T = int(input())
for _ in range(T):
    N, A, B, C, D = map(int, input().split())
    print(solve(N, A, B, C, D))
