# https://atcoder.jp/contests/abc130/tasks/abc130_c

W, H, x, y = map(int, input().split())

if W - 2*x == 0:
    if H - 2*y == 0:
        high = H/2
    else:
        high = 0
else:
    high = (H*W - W*y - H*x) / (W - 2*x)     # 縦に2分割する時の、Wのy座標
# print(high)

if H - 2*y == 0:
    if W - 2*x == 0:
        width = W/2
    else:
        width = 0
else:
    width =  (H*W - W*y - H*x) / (H - 2*y)   # 横に2分割する時の、Hのx座標
# print(width)

if (high > 0 and high < H) and (width > 0 and width < W):
    ans = 1
else:
    ans = 0
    
print(W*H/2, ans)
