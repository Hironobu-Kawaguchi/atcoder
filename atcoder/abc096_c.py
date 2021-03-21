# https://atcoder.jp/contests/abc096/tasks/abc096_c

def check(i, j, s, H, W):
    if i != 0:
        if s[i-1][j] == '#':
            return True
    if i != H-1:
        if s[i+1][j] == '#':
            return True
    if j != 0:
        if s[i][j-1] == '#':
            return True
    if j != W-1:
        if s[i][j+1] == '#':
            return True
    return False

H, W = map(int, input().split())

s = []
for i in range(H):
    s.append(input())

ans = 'Yes'
for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            if check(i, j, s, H, W) == False:
                ans = 'No'

print(ans)
