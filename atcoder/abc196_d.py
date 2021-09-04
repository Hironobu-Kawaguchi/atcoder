# https://atcoder.jp/contests/abc196/tasks/abc196_d

import sys
sys.setrecursionlimit(10 ** 7)

H, W, A, B = map(int, input().split())
assert H*W==A*2+B
ans = 0

def dfs(i, bit, A, B):
    if i==H*W:
        global ans
        ans += 1
        return
    if bit>>i & 1:
        dfs(i+1, bit, A, B)
        return
    if B:
        dfs(i+1, bit | 1<<i, A, B-1)
    if A:
        if i%W != W-1 and not bit>>(i+1) & 1:
            dfs(i+1, bit | 1<<i | 1<<(i+1), A-1, B)
        if i//W != H-1 and not bit>>(i+W) & 1:
            dfs(i+1, bit | 1<<i | 1<<(i+W), A-1, B)
    
dfs(0,0,A,B)
print(ans)


# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

# H, W, A, B = map(int, input().split())
# used = [[False]*16 for _ in range(16)]

# def dfs(i, j, a, b):
#     global used
#     if (a<0 or b<0): return 0
#     if (j==W):
#         j = 0
#         i += 1
#     if (i==H): return 1
#     if used[i][j]: return dfs(i, j+1, a, b)        
#     res = 0
#     used[i][j] = True
#     res += dfs(i, j+1, a, b-1)
#     if (j<W-1 and not used[i][j+1]):
#         used[i][j+1] = True
#         res += dfs(i, j+1, a-1, b)
#         used[i][j+1] = False
#     if (i<H-1 and not used[i+1][j]):
#         used[i+1][j] = True        
#         res += dfs(i, j+1, a-1, b)
#         used[i+1][j] = False
#     used[i][j] = False
#     return res

# print(dfs(0,0, A, B))
