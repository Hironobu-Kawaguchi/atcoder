# https://codeforces.com/contest/1326/problem/A

def main(n):
    if n==1:
        return -1
    else:
        return '2' + '9'*(n-1)

t = int(input())
for i in range(t):
    n = int(input())
    print(main(n))


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
