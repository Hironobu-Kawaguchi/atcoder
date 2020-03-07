# https://atcoder.jp/contests/abc158/tasks/abc158_a

import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

S = input()
ans = "No"
for i in range(2):
    if S[i] != S[i+1]:
        ans = "Yes"
print(ans)
