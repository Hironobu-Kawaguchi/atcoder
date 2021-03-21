# https://codeforces.com/contest/1334/problem/A

def main():
    n = int(input())
    p, c = [0], [0]
    for i in range(n):
        _p, _c = map(int, input().split())
        p.append(_p)
        c.append(_c)
    for i in range(n):
        dif_p = p[i+1] - p[i]
        dif_c = c[i+1] - c[i]
        if dif_p < 0 or dif_c < 0 or dif_p < dif_c:
            return "No"
    return "Yes"

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
