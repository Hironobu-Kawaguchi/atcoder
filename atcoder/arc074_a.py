# https://atcoder.jp/contests/abc062/tasks/arc074_a

H, W = map(int, input().split())
ans = H*W

if H % 3 == 0:
    ans = 0
else:
    ans = min(ans, W)

if W % 3 == 0:
    ans = 0
else:
    ans = min(ans, H)

for i in range(1, H):
    if W % 2 == 0:
        dif = abs(i*W - (H-i)*(W//2))
    else:
        dif = max(i*W, (H-i)*((W//2)+1)) - min(i*W, (H-i)*(W//2))
    ans = min(ans, dif)

for i in range(1, W):
    if H % 2 == 0:
        dif = abs(i*H - (W-i)*(H//2))
    else:
        dif = max(i*H, (W-i)*((H//2)+1)) - min(i*H, (W-i)*(H//2))
    ans = min(ans, dif)

print(ans)
