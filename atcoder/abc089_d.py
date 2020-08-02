# https://atcoder.jp/contests/abc089/tasks/abc089_d

H, W, D = map(int, input().split())
px = [0] * (H*W+1)
py = [0] * (H*W+1)
d = [0] * (H*W+1)

for y in range(H):
    line = list(map(int, input().split()))
    for x, A in enumerate(line):
        px[A] = x
        py[A] = y

for i in range(D+1, H*W+1):
    d[i] = d[i-D] + abs(px[i]-px[i-D]) + abs(py[i]-py[i-D])

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    print(d[R]-d[L])
