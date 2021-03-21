# https://codeforces.com/contest/1325/problem/A

# import sys
# # input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

# from fractions import gcd
# def f(a, b):
#     _gcd = gcd(a, b)
#     _lcm = (a*b) // _gcd
#     return _gcd + _lcm

# def main(x):
#     for a in range(1, x):
#         for b in range(a, x):
#             if f(a, b) == x:
#                 print(a, b)
#                 return

t = int(input())
for i in range(t):
    x = int(input())
    # main(x)
    print(1, x-1)
