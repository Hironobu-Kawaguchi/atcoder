# C - 2D Plane 2N Points
# https://atcoder.jp/contests/abc091/tasks/arc092_a

N = int(input())
ab = []
for i in range(N):
    _a, _b = map(int, input().split())
    ab.append((_a, _b))
cd = []
for j in range(N):
    _c, _d = map(int, input().split())
    cd.append((_c, _d))
cd.sort()

s = set()
for j in range(N):
    maxb = -1
    maxi = -1
    for i in range(N):
        if ab[i][0] < cd[j][0] and ab[i][1] < cd[j][1] and i not in s:
            if ab[i][1] > maxb:
                maxb = ab[i][1]
                maxi = i
    if maxi != -1:
        s.add(maxi)
print(len(s))


# N = int(input())
# a, b = [], []
# for i in range(N):
#     _a, _b = map(int, input().split())
#     a.append(_a)
#     b.append(_b)
# c, d = [], []
# for j in range(N):
#     _c, _d = map(int, input().split())
#     c.append(_c)
#     d.append(_d)

# ans = 0
# for i in range(N):
#     for j in range(N):
#         if a[i] < c[j] and b[i] < d[j]:
#             ans += 1

# print(ans)
