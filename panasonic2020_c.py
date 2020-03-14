# https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_c

# import sys
# # input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

# import math
a, b, c = map(int, input().split())
# if math.sqrt(a) + math.sqrt(b) < math.sqrt(c):
# if a + b + 2 * math.sqrt(a*b) < c:
if c-a-b < 0:
    print("No")
elif 4*a*b < (c-a-b)**2:
    print("Yes")
else:
    print("No")
