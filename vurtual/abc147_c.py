# https://atcoder.jp/contests/abc147/tasks/abc147_c
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

N = int(input())
ys = [[-1]*N for _ in range(N)]
for i in range(N):
    A = int(input())
    for j in range(A):
        x, y = map(int, input().split())
        ys[i][x-1] = y
# print(ys)

ans = 0
for b in range(1<<N):
    chk = [-1] * N      # 1: 正直 0:不親切
    flg = True
    for i in range(N):
        if b>>i&1:
            if chk[i] == 0:
                flg = False
                break
            chk[i] = 1
            for j in range(N):
                if ys[i][j] == -1: continue
                if chk[j] != -1 and chk[j] != ys[i][j]:
                    flg = False
                    break
                chk[j] = ys[i][j]
        else:
            if chk[i] == 1:
                flg = False
                break
            chk[i] = 0
    if flg:
        ans = max(ans, sum(chk))    # chk が 1の数
print(ans)


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
