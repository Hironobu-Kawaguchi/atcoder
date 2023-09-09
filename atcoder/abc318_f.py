# https://atcoder.jp/contests/abc318/tasks/abc318_d
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
import bisect

N = int(input())
X = list(map(int, input().split()))
L = list(map(int, input().split()))

def check(k):
    # k: タコ型ロボットの頭を置く座標
    X_copy = X.copy()

    for i in range(N):
        idx = bisect.bisect_right(X_copy, k)
        if idx >= len(X_copy):
            idx -= 1
        elif idx == 0:
            pass
        else:
            if abs(X_copy[idx] - k) > abs(X_copy[idx-1] - k):
                idx -= 1
        if abs(X_copy[idx] - k) > L[i]:
            # print(k, i, idx, X_copy, abs(X_copy[idx] - k), L[i], file=sys.stderr)
            return False
        X_copy.pop(idx)

    return True  # 全ての宝石を掴める

check_points = []
for i in range(N):
    for j in range(N):
        for sign in [-1, 1]:
            check_points.append(X[i] + sign*L[j] - 1)
            check_points.append(X[i] + sign*L[j])
            check_points.append(X[i] + sign*L[j] + 1)
check_points = list(set(check_points))
check_points.sort()

check_flg = []
for k in check_points:
    check_flg.append(check(k))
# print(list(zip(check_points, check_flg)), file=sys.stderr)

ans = 0
for i in range(len(check_points) - 1):
    if check_flg[i] and check_flg[i+1]:
        ans += check_points[i+1] - check_points[i]
    elif check_flg[i] and not check_flg[i+1]:
        ans += 1
print(ans)
