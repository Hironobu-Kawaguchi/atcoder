# https://codeforces.com/contest/1547/problem/C

# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
INF = 1001

def main():
    input()
    k, n, m = map(int, input().split())
    a = list(map(int, (input().split())))
    a.append(INF)
    b = list(map(int, (input().split())))
    b.append(INF)
    # print(a, b)
    i, j = 0, 0
    ok = True
    ans = []
    while i+j+1<=n+m:
        if a[i]<=b[j]:
            if k<a[i]:
                # print('a', k, i+j, i, a[i])
                ok = False
                break
            else:
                if a[i]==0:
                    k += 1
                ans.append(a[i])
                i += 1
        else:
            if k<b[j]:
                # print('b', k, i+j, j, b[j])
                ok = False
                break
            else:
                if b[j]==0:
                    k += 1
                ans.append(b[j])
                j += 1
    # print(ans)
    if ok:
        print(*ans)
    else:
        print(-1)
    return

t = int(input())
for _ in range(t):
    main()


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
