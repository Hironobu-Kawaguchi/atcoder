# https://atcoder.jp/contests/agc043/tasks/agc043_a
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
S = [input() for _ in range(H)]
# print(S)
INF = 1001001001

dp = [[INF]*W for _ in range(H)]
if S[0][0] == '#':
    dp[0][0] = 1
else:
    dp[0][0] = 0

for r in range(H):
    for c in range(W):
        if r:
            if S[r][c] == '#' and S[r-1][c] == '.':
                dp[r][c] = min(dp[r][c], dp[r-1][c]+1)
            else:
                dp[r][c] = min(dp[r][c], dp[r-1][c])
        if c:
            if S[r][c] == '#' and S[r][c-1] == '.':
                dp[r][c] = min(dp[r][c], dp[r][c-1]+1)
            else:
                dp[r][c] = min(dp[r][c], dp[r][c-1])

print(dp[H-1][W-1])



# H, W = map(int, input().split())
# S = [input() for _ in range(H)]
# # print(S)
# dr = [ 1, 0]
# dc = [ 0, 1]
# ans = 1001001001

# def dfs(r,c,cnt,flg):
#     """
#     r, c
#     cnt: 連続黒の回数
#     flg: 1: 現在白（黒に来たらcnt+1）, 0: 現在黒
#     """
#     global ans
#     if S[r][c] == '#':
#         if flg:
#             cnt += 1
#             black_flg = 0
#     else:
#         flg = 1

#     if r==H-1 and c ==W-1:
#         ans = min(ans, cnt)
#         return

#     for dir in range(2):
#         nr = r + dr[dir]
#         nc = c + dc[dir]
#         if nr >= H or nc >= W: continue
#         dfs(nr, nc, cnt, flg)
#     return

# dfs(0,0,0,1)
# print(ans)
