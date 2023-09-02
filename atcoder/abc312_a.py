# https://atcoder.jp/contests/abc312/tasks/abc312_a

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

S = input()
lst = ["ACE", "BDF", "CEG", "DFA", "EGB", "FAC","GBD"]
if S in lst:
    print("Yes")
else:
    print("No")
    