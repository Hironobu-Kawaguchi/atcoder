# https://atcoder.jp/contests/abc088/tasks/abc088_c

c = [[int(i) for i in input().split()] for _ in range(3)]

ans = 'Yes'
if c[0][0] - c[0][1] != c[1][0] - c[1][1] or c[0][0] - c[0][1] != c[2][0] - c[2][1]:
    ans = 'No'
if c[0][0] - c[0][2] != c[1][0] - c[1][2] or c[0][0] - c[0][2] != c[2][0] - c[2][2]:
    ans = 'No'
if c[0][0] - c[1][0] != c[0][1] - c[1][1] or c[0][0] - c[1][0] != c[0][2] - c[1][2]:
    ans = 'No'
if c[0][0] - c[2][0] != c[0][1] - c[2][1] or c[0][0] - c[2][0] != c[0][2] - c[2][2]:
    ans = 'No'

print(ans)
