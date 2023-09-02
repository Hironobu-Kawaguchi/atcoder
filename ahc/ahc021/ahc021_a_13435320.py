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

def solve(r_list):
    b = copy.copy(b_o)
    c = copy.copy(c_o)
    ans = []

    def ball_swap(x1, y1, x2, y2):
        b[xy2i(x1, y1)], b[xy2i(x2, y2)] = b[xy2i(x2, y2)], b[xy2i(x1, y1)]
        c[b[xy2i(x1, y1)]], c[b[xy2i(x2, y2)]] = c[b[xy2i(x2, y2)]], c[b[xy2i(x1, y1)]]
        ans.append([x1, y1, x2, y2])
        # print(len(ans), ans[-1], b[xy2i(x1, y1)], file=sys.stderr)
        return

    per = []
    now = 0
    for i in range(N2 - len(r_list)):
        if now<len(r_list) and i==r_list[now]:
            per.append((N2-now-1, False))
            per.append((i, True))
            now += 1
        else:
            per.append((i, True))
    if now<len(r_list):
        for i in range(now, len(r_list)):
            per.append((N2-i-1, False))
    
    # print(len(per), per[:10], file=sys.stderr)
    assert len(per)==N2
    for i, t in per:
        x, y = xy[c[i]]
        if t:
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
                if i > b[xy2i(nx, ny)]: break
                ball_swap(nx, ny, x, y)
                x, y = nx, ny
        else:
            while x<N-1:
                nx = x+1
                if b[xy2i(x+1, y)]>b[xy2i(x+1, y+1)]:
                    ny = y+1
                else:
                    ny = y
                if i < b[xy2i(nx, ny)]: break
                ball_swap(nx, ny, x, y)
                x, y = nx, ny
    return ans

anss = []
r_list = []

anss.append(solve(r_list))
best_K = len(anss[0])
now = 0
while time.time()-start<1.6:
# while time.time()-start<0.1:
    if now>=N2-len(r_list): break
    while time.time()-start<1.6:
        ans = solve(r_list + [now])
        # print(now, len(ans), best_K, len(r_list), r_list, file=sys.stderr)
        # print(now, len(ans), best_K, len(r_list), file=sys.stderr)
        if len(ans)<best_K:
            anss.append(ans)
            best_K = len(ans)
            r_list.append(now)
            now += 1
            break
        now += 1
        if now>=N2-len(r_list): break

K = 10000
for idx, ans in enumerate(anss):
    # print(idx, len(ans), r_list, file=sys.stderr)
    if len(ans)<K:
        K = len(ans)
        ans_idx = idx
if ans_idx>0:
    print("*" * 100, file=sys.stderr)
print(len(anss[ans_idx]))
for x1, y1, x2, y2 in anss[ans_idx]:
    print(x1, y1, x2, y2)
