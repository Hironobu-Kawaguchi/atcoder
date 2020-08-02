# https://atcoder.jp/contests/agc045/tasks/agc045_a
# https://atcoder.jp/contests/agc045/submissions/14092765
import sys
from numba import njit
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit('(i8,)', cache=True)
def keta(x):
    ret = -1
    while x >= 1:
        x >>= 1
        ret += 1
    return ret

@njit('(i8,i8[::1],i4[::1])', cache=True)
def solve(N, A, S):
    if np.all(S == 0):
        return True
    if S[-1] == 1:
        if A[-1] == 0:
            return solve(N - 1, A[:-1], S[:-1])
        else:
            return False
    # .....10000
    i = np.where(S == 1)[0].max() + 1
    A1 = A[:i]
    B = A[i:]
    while True:
        B = B[B != 0]
        if len(B) == 0:
            break
        x = B.max()
        k = keta(x)
        A1 ^= ((A1 >> k) & 1) * x
        B ^= ((B >> k) & 1) * x
    N = len(A1)
    return solve(N, A1, S[:N])

def main():
    T = int(readline())
    for _ in range(T):
        N = int(readline())
        A = np.array(readline().split(), np.int64)
        S = np.array(list(readline().decode().rstrip()), np.int32)
        x = 0 if solve(N, A, S) else 1
        print(x)

main()
