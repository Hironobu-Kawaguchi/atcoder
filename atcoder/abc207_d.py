# https://atcoder.jp/contests/ABC207/tasks/abc207_d

import math

def main():
    N = int(input())
    ab = []
    center_ab = [0, 0]
    for i in range(N):
        a, b = map(int, input().split())
        center_ab[0] += a
        center_ab[1] += b
        ab.append([a*N,b*N])
    # print(center_ab, ab)
    for i in range(N):
        for j in range(2):
            ab[i][j] -= center_ab[j]
    # print(ab)

    cd = []
    center_cd = [0, 0]
    for i in range(N):
        c, d = map(int, input().split())
        center_cd[0] += c
        center_cd[1] += d
        cd.append([c*N,d*N])
    # print(center_cd, cd)
    for i in range(N):
        for j in range(2):
            cd[i][j] -= center_cd[j]
    # print(cd)

    for i in range(N):
        if ab[i][0]!=0 or ab[i][1]!=0:
            ab[i][0], ab[0][0] = ab[0][0], ab[i][0]
            ab[i][1], ab[0][1] = ab[0][1], ab[i][1]

    ans = "No"
    eps = 1e-6
    for i in range(N):
        angle = math.atan2(cd[i][1], cd[i][0]) - math.atan2(ab[0][1], ab[0][0])
        flag = True
        for j in range(N):
            x = ab[j][0] * math.cos(angle) - ab[j][1] * math.sin(angle)
            y = ab[j][0] * math.sin(angle) + ab[j][1] * math.cos(angle)
            flag2 = False
            for k in range(N):
                if abs(cd[k][0]-x)<=eps and abs(cd[k][1]-y)<=eps:
                    flag2 = True
            flag &= flag2
        if flag:
            ans = "Yes"

    print(ans)

main()
