# https://codeforces.com/contest/1334/problem/B

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    cum = 0
    for i in range(n):
        cum += a[i]
        if cum < x * (i+1):
            return i
    return n

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
