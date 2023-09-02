# https://atcoder.jp/contests/abc313/tasks/abc313_d
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
A = [0]*N

def f(x):
    print("?", *[y+1 for y in x], flush=True)
    res = int(input())
    return res

B = [0]*(K+1)
t = 0
for i in range(K+1):
    x = []
    for j in range(K+1):
        if i==j: continue
        x.append(j)
    B[i] = f(x)
    t ^= B[i]
for i in range(K+1):
    A[i] = t ^ B[i]

t = 0
for i in range(K-1): t ^= A[i]
for i in range(K+1, N):
    x = []
    for j in range(K-1): x.append(j)
    x.append(i)
    A[i] = t ^ f(x)

print("!", *A)



# WA
# N, K = map(int, input().split())
# idxs = list(range(1, N+1))
# ts = []

# for i in range(N):
#     if K+i < N:
#         xs = idxs[i:K+i]
#     else:
#         xs = idxs[0:(K+i)%N] + idxs[i:]
#     print("?", *xs, flush=True)
#     T = int(input())
#     ts.append(T)

# print(ts, file=sys.stderr)

# A = [-1]*N

# def check_A(si=0):
#     t = 0
#     for i in range(si, si+K):
#         t ^= A[i%N]
#     return t==ts[si]

# def create_A(si=0, sv=0):
#     A[si] = sv
#     for j in range(N):
#         i = (si + j*K) % N
#         tmp = (ts[i%N] ^ ts[(i+1)%N]) ^ A[i%N]
#         if A[(i+K)%N]==-1:
#             A[(i+K)%N] = tmp
#         elif A[(i+K)%N]!=tmp:
#             return False
#     ok = check_A(si)
#     return ok

# for i in range(N):
#     if A[i]!=-1: continue
#     for sv in range(2):
#         flg = create_A(sv)
#         print(flg, A, file=sys.stderr)
#         if flg: break
# print("!", *A)
