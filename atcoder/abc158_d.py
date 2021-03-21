# https://atcoder.jp/contests/abc158/tasks/abc158_d

import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

reverse = 0
pre = []
after = []
S = input()
Q = int(input())
for i in range(Q):
    q = input()
    if q[0] == '1':
        reverse = 1 - reverse
    else:
        T, F, C = q.split()
        if (F == '1') ^ (reverse == 1):
            pre.append(C)
        else:
            after.append(C)
if reverse:
    after.reverse()
    ans = ''.join(after) + S[::-1] + ''.join(pre)
else:
    pre.reverse()
    ans = ''.join(pre) + S + ''.join(after)
print(ans)
