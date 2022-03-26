# https://atcoder.jp/contests/ahc009/tasks/ahc009_a

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import time
start = time.time()

import random
import copy

si, sj, ti, tj, p = input().split()
si = int(si); sj = int(sj); ti = int(ti); tj = int(tj)
p = float(p)
h = [input() for _ in range(20)]
v = [input() for _ in range(19)]

def solve():
    # pd + pu * pr * pl = 1.0
    # (pd - pu) * 200 * (1-p) = ti - si
    # (pr - pl) * 200 * (1-p) = tj - sj
    # move = (1-p)*150
    # (ti-si+tj-sj)
    ans = random.choices(
            ['U', 'D', 'L', 'R'], [1, p*10+2, 1, p*10+2], k=150)
    # ans = random.choices(
    #         ['U', 'D', 'L', 'R'], 
    #         [(ti-si)*(1-p)*(ti-si+tj-sj)/150, (ti-si)*(1-p)*(ti-si+tj-sj)/150/p,
    #          (tj-sj)*(1-p)*(ti-si+tj-sj)/150, (tj-sj)*(1-p)*(ti-si+tj-sj)/150/p],
    #         k=150)
    ans.extend(random.choices(['U', 'D', 'L', 'R'], [1, 2, 1, 2], k=50))
    return ans

def calc_point(ans):
    es = 0.0
    nxt = [[0]*20 for _ in range(20)]
    nxt[si][sj] = 1
    for t, c in enumerate(ans):
        now = copy.copy(nxt)
        nxt = [[0]*20 for _ in range(20)]
        for i in range(20):
            for j in range(20):
                if c=='U':
                    if i==0 or v[i-1][j]=='1':
                        nxt[i][j] += now[i][j]
                    else:
                        nxt[i][j] += now[i][j] * p
                        nxt[i-1][j] += now[i][j] * (1-p)
                elif c=='D':
                    if i==19 or v[i][j]=='1':
                        nxt[i][j] += now[i][j]
                    else:
                        nxt[i][j] += now[i][j] * p
                        nxt[i+1][j] += now[i][j] * (1-p)
                elif c=='L':
                    if j==0 or h[i][j-1]=='1':
                        nxt[i][j] += now[i][j]
                    else:
                        nxt[i][j] += now[i][j] * p
                        nxt[i][j-1] += now[i][j] * (1-p)
                else:
                    if j==19 or h[i][j]=='1':
                        nxt[i][j] += now[i][j]
                    else:
                        nxt[i][j] += now[i][j] * p
                        nxt[i][j+1] += now[i][j] * (1-p)
        es += nxt[ti][tj] * (400-t)
        nxt[ti][tj] = 0
    return round(250000*es)

best_ans = ''
best_point = -1
while time.time() < start + 1.8:
    ans = solve()
    point = calc_point(ans)
    # print(point, best_point, time.time() - start)
    if point > best_point:
        best_point = point
        best_ans = copy.copy(ans)

print(''.join(best_ans))
