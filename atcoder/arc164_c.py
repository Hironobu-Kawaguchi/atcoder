# https://atcoder.jp/contests/arc164/tasks/arc164_c
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
AB = []
ans = 0
cnt_good = 0
for i in range(N):
    A, B = map(int, input().split())
    AB.append((abs(A-B), A, B))
    ans += max(A, B)
    if A>=B:
        cnt_good += 1
AB.sort()
if cnt_good % 2 == 1:
    ans -= AB[0][0]
print(ans)
