# C - Infinite Grid
# https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_c

H, W = map(int, input().split())
c = []
cnt = 0
for h in range(H):
    tmp = list(input())
    cnt += tmp.count('#')
    tmp = tmp + tmp
    c.append(tmp)

if cnt >= H:
    print(':(')
else:
    print('Yay!')