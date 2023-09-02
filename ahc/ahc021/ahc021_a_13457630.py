# https://atcoder.jp/contests/ahc021/tasks/ahc021_a

import sys
import copy
import random
import time
start = time.time()

N = 30
N2 = N*(N+1)//2
b_o = []
for i in range(N):
    b_o.extend(list(map(int, input().split())))
# print(b_o, file=sys.stderr)

c_o = [-1] * N2
for i in range(N2):
    c_o[b_o[i]] = i
# print(c_o, file=sys.stderr)

xy = []
for x in range(N):
    for y in range(x+1):
        xy.append((x, y))
# print(xy, file=sys.stderr)

def xy2i(x, y):
    return x*(x+1)//2 + y

def solve(p):
    b = copy.copy(b_o)
    c = copy.copy(c_o)
    ans = []

    def ball_swap(x1, y1, x2, y2):
        b[xy2i(x1, y1)], b[xy2i(x2, y2)] = b[xy2i(x2, y2)], b[xy2i(x1, y1)]
        c[b[xy2i(x1, y1)]], c[b[xy2i(x2, y2)]] = c[b[xy2i(x2, y2)]], c[b[xy2i(x1, y1)]]
        ans.append([x1, y1, x2, y2])
        # print(len(ans), ans[-1], b[xy2i(x1, y1)], file=sys.stderr)
        return

    l, r = 0, N2-1
    while l<r+1:
        t = random.random()<p
        # print(l, r, t, file=sys.stderr)
        if t:
            x, y = xy[c[l]]
            l += 1
            while x>0:
                nx = x-1
                if y==0:
                    ny = 0
                elif y == x:
                    ny = y-1
                elif b[xy2i(x-1, y-1)]>b[xy2i(x-1, y)]:
                    ny = y-1
                else:
                    ny = y
                if l > b[xy2i(nx, ny)]: break
                ball_swap(nx, ny, x, y)
                x, y = nx, ny
        else:
            x, y = xy[c[r]]
            r -= 1
            while x<N-1:
                nx = x+1
                if b[xy2i(x+1, y)]>b[xy2i(x+1, y+1)]:
                    ny = y+1
                else:
                    ny = y
                if r < b[xy2i(nx, ny)]: break
                ball_swap(nx, ny, x, y)
                x, y = nx, ny
    return ans, p

anss = []
anss.append(solve(p=1.0))
while time.time()-start<1.6:
    anss.append(solve(p=1 - random.random()**4))
    # anss.append(solve(p=random.uniform(0.9, 1.0)))
    # anss.append(solve(p=0.95))
    # anss.append(solve(p=0.9))
    # anss.append(solve(p=0.5))
    # anss.append(solve(p=0.0))

K = 10000
for idx, (ans, p) in enumerate(anss):
    # print(idx, len(ans), p, file=sys.stderr)
    if len(ans)<K:
        K = len(ans)
        ans_idx = idx
if ans_idx>0:
    print("*" * 100, file=sys.stderr)
print(len(anss[ans_idx][0]))
for x1, y1, x2, y2 in anss[ans_idx][0]:
    print(x1, y1, x2, y2)
