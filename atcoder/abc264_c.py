# https://atcoder.jp/contests/abc264/tasks/abc264_c
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

from itertools import combinations

HA, WA = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(HA)]
HB, WB = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(HB)]

hd, wd  = HA - HB, WA - WB
if hd < 0 or wd < 0:
    print('No')
    exit()

def change(A, hs, ws):
    ret = []
    for i in range(HA):
        if i in hs: continue
        line = []
        for j in range(WA):
            if j in ws: continue
            line.append(A[i][j])
        ret.append(line)
    return ret

for hs in combinations(range(HA), hd):
    for ws in combinations(range(WA), wd):
        # print(hs, ws)
        A_ = change(A, hs, ws)
        if A_ == B:
            print('Yes')
            exit()
print('No')
