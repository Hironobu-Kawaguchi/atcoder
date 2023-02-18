# https://atcoder.jp/contests/arc145/tasks/arc145_a

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input()

if (S[0]=='A' and S[-1]=='B') or S=="BA":
    print("No")
else:
    print("Yes")
