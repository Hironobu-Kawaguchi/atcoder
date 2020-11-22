# https://atcoder.jp/contests/abc184/tasks/abc184_c
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()

r1,c1 = map(int, input().split())
r2,c2 = map(int, input().split())

def chk(r1,c1,r2,c2):
    """ 3マス以内移動後に、斜めで1回で行けるか """
    for x in range(-2, 3):
        for y in range(-2, 3):
            if (r1+x)+(c1+y)==r2+c2 or (r1+x)-(c1+y)==r2-c2:
                return True
    for x in [-3,3]:
        if (r1+x)+c1==r2+c2 or (r1+x)-c1==r2-c2:
            return True
    for y in [-3,3]:
        if r1+(c1+y)==r2+c2 or r1-(c1+y)==r2-c2:
            return True
    return False

if r1==r2 and c1==c2:
    ans = 0
elif (r1+c1==r2+c2) or (r1-c1==r2-c2) or (abs(r1-r2)+abs(c1-c2)<=3):
    ans = 1
elif ((r1+c1)%2==(r2+c2)%2) or (abs(r1-r2)+abs(c1-c2)<=6) or chk(r1,c1,r2,c2):
    ans = 2
else:
    ans =3

print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
