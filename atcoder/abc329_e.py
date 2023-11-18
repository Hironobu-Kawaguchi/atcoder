# https://atcoder.jp/contests/abc329/tasks/abc329_e

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

N, M = map(int, (input().split()))
S = list(input())
T = list(input())

used = [False] * N

def ok(pos):
    if pos < 0 or pos + M > N:
        return False
    for i in range(M):
        if S[i + pos] != '#' and S[i + pos] != T[i]:
            return False
    return True

def dfs(pos):
    used[pos] = True
    S[pos:pos+M] = ['#'] * M
    # print(pos, "".join(S), file=sys.stderr)
    for i in range(pos - M + 1, pos + M):
        if ok(i) and not used[i]:
            dfs(i)

for i in range(N):
    if ok(i) and not used[i]:
        dfs(i)

if all(s == '#' for s in S):
    print("Yes")
else:
    print("No")



# TLE
# N, M = map(int, (input().split()))
# S = list(input())
# T = list(input())

# def check(s, t):
#     for i in range(M):
#         if s[i] != '#' and s[i] != t[i]:
#             return False
#     return True

# while True:
#     flg = False
#     for i in range(N-M+1):
#         if not all(s == '#' for s in S[i:i+M]) and check(S[i:i+M], T):
#             S[i:i+M] = ['#'] * M
#             flg = True
#     if not flg:
#         break

# if all(s == '#' for s in S):
#     print("Yes")
# else:
#     print("No")
