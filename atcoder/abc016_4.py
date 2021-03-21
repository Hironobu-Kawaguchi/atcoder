# https://atcoder.jp/contests/abc016/tasks/abc016_4

from collections import namedtuple
xy = namedtuple('xy',('x', 'y'))    # x,y を格納するtuple
Ax, Ay, Bx, By = map(int, input().split())
a = xy(Ax, Ay)
b = xy(Bx, By)
N = int(input())
vertex = [xy(*map(int, input().split())) for _ in range(N)]

def side(a, b, c):
    """ c は 直線ab のどちら側か """
    x1 = c.x- a.x
    x2 = c.x- b.x
    y1 = c.y- a.y
    y2 = c.y- b.y
    return x1*y2 - x2*y1    # 符号付き面積（1/2はしていない）

def is_cross(a, b, c, d):
    """ ab と cd は交差しているか """
    chk1 = side(a,b,c) * side(a,b,d) < 0    # c,d は ab の逆側
    chk2 = side(c,d,a) * side(c,d,b) < 0    # a,b は cd の逆側
    return chk1 and chk2                    # 両方を満たしていれば交差

vertex += [vertex[0]]
cnt = sum(is_cross(a,b,c,d) for c,d in zip(vertex[:-1], vertex[1:]))
ans = cnt//2 + 1    # 交差している数の1/2回分割されるので、＋1分割になる
print(ans)
