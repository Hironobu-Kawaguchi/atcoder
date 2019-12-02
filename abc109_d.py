# https://atcoder.jp/contests/abc109/tasks/abc109_d

H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]

yx = []
for i in range(H*W):
    y = i // W
    x = W - i % W - 1 if y % 2 else i % W 
    yx.append((y, x))

ans = []
for i in range(H*W-1):
    y, x = yx[i]
    if a[y][x] % 2:
        yd, xd = yx[i+1]
        a[y][x] -= 1
        a[yd][xd] += 1
        ans.append((y+1, x+1, yd+1, xd+1))

n = len(ans)
print(n)
for i in range(n):
    print(*ans[i])
