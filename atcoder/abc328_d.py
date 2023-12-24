# https://atcoder.jp/contests/abc328/tasks/abc328_d

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

S = input()

ans = []
for c in S:
    ans.append(c)
    if len(ans) >= 3 and ans[-1] == 'C' and ans[-2] == 'B' and ans[-3] == 'A':
        ans.pop()
        ans.pop()
        ans.pop()
print("".join(ans))
