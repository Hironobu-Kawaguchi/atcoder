# https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_e

from itertools import permutations, product
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

MX = 2005
d = [[[0]*MX for _ in range(3)] for _ in range(3)]
# print(d)

s = [input() for _ in range(3)]
s.sort()
# print(s)

ans = MX*3
for sss in permutations(s):
    # print(sss)
    for i, j in product(range(3), repeat=2):
        for k in range(len(sss[i])):
            if i >= j: continue
            # print(i,j,k)
            ok = True
            for ni in range(k, len(sss[i])):
                nj = ni - k
                if nj >= len(sss[j]): break
                if sss[i][ni] == '?' or sss[j][nj] == '?': continue
                if sss[i][ni] != sss[j][nj]: ok = False
            d[i][j][k] = ok
    def f(i, j, k):
        if k >= len(sss[i]):
            return True
        return d[i][j][k]
    # print(sss)
    for x, y in product(range(MX), repeat=2):
        if f(0,1,x) == False: continue
        if f(1,2,y) == False: continue
        if f(0,2,x+y) == False: continue
        now = 0
        now = max(now, len(sss[0]))
        now = max(now, x+len(sss[1]))
        now = max(now, x+y+len(sss[2]))
        ans = min(ans, now)
print(ans)
