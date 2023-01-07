# https://atcoder.jp/contests/typical90/tasks/typical90_f

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
S = input()
# print(S)

# c[i][j] i文字目以降にj=ord[文字]-ord['a]がでてくるindex
c = [[-1]*26 for _ in range(N)]

for i in range(N-1, -1, -1):
    ch = ord(S[i]) - ord('a')
    for j in range(26):
        if j==ch:
            c[i][j] = i
        elif i!=N-1:
            c[i][j] = c[i+1][j]
# print(c)

ans = ''
num = 0
i = 0
while num<K:
    # print(i, num, ans)
    for j in range(26):
        # print(i, j)
        if c[i][j]==-1: continue
        if N-c[i][j]>=K-num:
            ans += chr(j+ord('a'))
            num += 1
            i = c[i][j] + 1
            break
print(ans)
