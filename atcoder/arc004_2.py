# B - 2点間距離の最大と最小 ( Maximum and Minimum )
# https://atcoder.jp/contests/arc004/tasks/arc004_2

N = int(input())
d = [int(input()) for _ in range(N)]

mx = max(d)
sm = sum(d)

print(sm)
print(max(0, mx - (sm - mx)))
