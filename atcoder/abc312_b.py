# https://atcoder.jp/contests/abc312/tasks/abc312_b

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
S = [input() for _ in range(N)]
# print(S, file=sys.stderr)

def check(si, sj):
    TaKCode =  ["###.?????",
                "###.?????",
                "###.?????",
                "....?????",
                "?????????",
                "?????....",
                "?????.###",
                "?????.###",
                "?????.###"
                ]
    for i in range(9):
        for j in range(9):
            if TaKCode[i][j] == "?": continue
            if TaKCode[i][j] != S[si+i][sj+j]:
                # print(si+i, sj+j, S[si+i][sj+j], i, j, TaKCode[i][j], file=sys.stderr)
                return False
    return True

ans = []
for si in range(N-8):
    for sj in range(M-8):
        if check(si, sj):
            ans.append((si, sj))
# print(ans, file=sys.stderr)

for si, sj in ans:
    print(si+1, sj+1)
