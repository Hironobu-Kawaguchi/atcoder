# https://atcoder.jp/contests/abc331/tasks/abc331_d
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)


N, Q = map(int, input().split())
P = [list(input()) for _ in range(N)]

cum = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        # cum[i+1][j+1] = cum[i+1][j] + int(P[i][j] == 'B')     ### TLE
        cum[i+1][j+1] = cum[i+1][j] + (1 if P[i][j] == 'B' else 0)
for j in range(N):
    for i in range(N):
        cum[i+1][j+1] += cum[i][j+1]

# for i in range(N+1):
#     print(cum[i], file=sys.stderr)

def f(y, x):
    y_div, y_mod = divmod(y, N)
    x_div, x_mod = divmod(x, N)
    ret = cum[N][N] * (y_div * x_div) + cum[N][x_mod] * y_div + cum[y_mod][N] * x_div + cum[y_mod][x_mod]
    # print(y, x, ret, file=sys.stderr)
    return ret

for qi in range(Q):
    A, B, C, D = map(int, input().split())
    ans = f(C+1, D+1) - f(C+1, B) - f(A, D+1) + f(A, B)
    print(ans)




# import sys
# # input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# # sys.setrecursionlimit(10 ** 7)

# N, Q = map(int, input().split())
# P = [list(input()) for _ in range(N)]

# cumP = [[0] * (N + 1) for _ in range(N + 1)]
# for i in range(N):
#     for j in range(N):
#         cumP[i + 1][j + 1] = cumP[i + 1][j] + (1 if P[i][j]=='B' else 0)
# # print(*cumP, file=sys.stderr)
# for j in range(N):
#     for i in range(N):
#         cumP[i + 1][j + 1] += cumP[i][j + 1]
# # for i in range(N):
# #     print(*cumP[i], file=sys.stderr)

# def g(h, w):
#     if h <= N and w <= N:
#         return cumP[h][w]
#     hq, hr = divmod(h, N)
#     wq, wr = divmod(w, N)
#     ret = hq * wq * cumP[N][N]
#     ret += hq * cumP[N][wr]
#     ret += wq * cumP[hr][N]
#     ret += cumP[hr][wr]
#     return ret

# def f(a, b, c, d):
#     return g(c, d) - g(c, b) - g(a, d) + g(a, b)


# for qi in range(Q):
#     A, B, C, D = map(int, input().split())
#     print(f(A, B, C + 1, D + 1))
