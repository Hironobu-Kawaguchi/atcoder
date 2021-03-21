# A - 2点間距離の最大値 ( The longest distance )
# https://arc004.contest.atcoder.jp/tasks/arc004_1
"""
平面上に N 個の点があり、それぞれ 0 から N−1 までの番号が付けられており、それぞれの点について x 座標と y 座標が与えられています。
その N 点のうち 2 点を選び結んで得られる線分のうち、最も長くなる線分の長さを求めてください。
"""
N = int(input())
xy = [[int(i) for i in input().split()] for _ in range(N)]
mx = 0
for i in range(N):
    for j in range(i+1, N):
        mx = max(mx, ((xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2) **(1/2))
print(mx)