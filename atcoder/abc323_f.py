# https://atcoder.jp/contests/abc323/tasks/abc323_f
# from numba import njit
# from functools import lru_cache

def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def adjust_x(xa, ya, xb, yb, xc, yc):
    if xb == xc:
        return 0, xa, ya, xb, yb
    elif xb < xc:
        xd, yd = xb - 1, yb
        d = dist(xa, ya, xd, yd)
        d += 2 if ya == yb and xa > xb else 0
        d += xc - xb
        return d, xc - 1, yb, xc, yb
    else:
        return adjust_x(-xa, ya, -xb, yb, -xc, yc)

XA, YA, XB, YB, XC, YC = map(int, input().split())
d1, xa1, ya1, xb1, yb1 = adjust_x(XA, YA, XB, YB, XC, YC)
d2 = adjust_x(ya1, xa1, yb1, xb1, YC, XC)[0]
d3, ya3, xa3, yb3, xb3 = adjust_x(YA, XA, YB, XB, YC, XC)
d4 = adjust_x(xa3, ya3, xb3, yb3, XC, YC)[0]
print(min(d1+d2, d3+d4))


# import sys
# # input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# # sys.setrecursionlimit(10 ** 7)

# Xa, Ya, Xb, Yb, Xc, Yc = map(int, input().split())
# # C > Bになるようにする
# if Xb > Xc:
#     Xa, Xb = Xa - (Xa- Xc) * 2, Xb - (Xb- Xc) * 2
# if Yb > Yc:
#     Ya, Yb = Ya - (Ya- Yc) * 2, Yb - (Yb- Yc) * 2


# # まずはXを合わせて，次にYを合わせる
# tmp = 0
# if Xb==Xc:
#     nx, ny = Xa, Ya
# else:
#     nx, ny = Xb - 1, Yb
#     tmp += abs(nx - Xa) + abs(ny - Ya)
#     if Ya == Yb and Xa > Xb:    tmp += 2    # 迂回が必要
#     tmp += Xc - Xb
#     nx = Xc - 1
# if Yb!=Yc:
#     tmp += abs(nx - Xc) + abs(ny - (Yb - 1))
#     if nx == Xc and ny > Yb:    tmp += 2    # 迂回が必要
#     tmp += Yc - Yb
# ans = tmp

# # Yを合わせて，次にXを合わせる
# tmp = 0
# if Yb==Yc:
#     nx, ny = Xa, Ya
# else:
#     nx, ny = Xb, Yb - 1
#     tmp += abs(nx - Xa) + abs(ny - Ya)
#     if Xa == Xb and Ya > Yb:    tmp += 2    # 迂回が必要
#     tmp += Yc - Yb
#     ny = Yc - 1
# if Xb!=Xc:
#     tmp += abs(nx - (Xb - 1)) + abs(ny - Yc)
#     if ny == Yc and nx > Xb:    tmp += 2    # 迂回が必要
#     tmp += Xc - Xb
# print(ans, tmp, file=sys.stderr)
# ans = min(ans, tmp)

# print(ans)
