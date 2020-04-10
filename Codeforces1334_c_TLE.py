# https://codeforces.com/contest/1334/problem/C

import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a, b = [], []
    for i in range(n):
        _a, _b = map(int, input().split())
        a.append(_a)
        b.append(_b)
    a.append(a[0])
    b.append(b[0])
    c = [max(0, a[-1]-b[-2])]
    d = [a[-1] - max(0, a[-1]-b[-2])]
    for i in range(n):
        c.append(max(0, a[i+1] - b[i]))
        d.append(a[i+1] - max(0, a[i+1] - b[i]))
    res = 0
    min_a = 10**12
    for i in range(n):
        if c[i] > 0:
            res += c[i]
            min_a = min(min_a, d[i])
        else:
            min_a = min(min_a, a[i])
    res += min_a
    return res

t = int(input())
for i in range(t):
    print(main())


# TLE
# def main(n):
#     i = 10**(n-1)
#     while i < 10**n:
#         flg = True
#         for j in range(n):
#             div = int(str(i)[j])
#             if div == 0:
#                 flg = False
#                 break
#             if i%div == 0:
#                 flg = False
#         if flg:
#             return i
#         else:
#             i += 1
#     return -1

# t = int(input())
# for i in range(t):
#     n = int(input())
#     print(main(n))
