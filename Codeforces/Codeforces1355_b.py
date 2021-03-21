# https://codeforces.com/contest/1355/problem/B

import sys
input = sys.stdin.buffer.readline

def main():
    n = int(input())
    e = list(map(int, input().split()))
    e.sort()

    ans = 0
    cur = 0
    for i in e:
        cur += 1
        if i <= cur:
            ans += 1
            cur = 0
    return ans

t = int(input())
for i in range(t):
    print(main())

# TLE
# def main():
#     n = int(input())
#     e = list(map(int, input().split()))
#     e.sort()
#     cum = [-1]*n
#     for i in range(n-1, -1, -1):
#         if i+1-e[i]>=0:
#             cum[i+1-e[i]] = e[i]
#     for i in range(n-2, -1, -1):
#         if cum[i] == -1 and cum[i+1] != -1:
#             cum[i] == cum[i+1]
#     res = 0
#     i = 0
#     # print(cum)
#     while i<n:
#         if cum[i] == -1:
#             i += 1
#         elif cum[i] <= n-i:
#             res += 1
#             i += cum[i]
#         else:
#             i += 1
#     return res

# t = int(input())
# for i in range(t):
#     print(main())

