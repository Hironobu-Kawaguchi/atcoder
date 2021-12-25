# https://atcoder.jp/contests/abc224/tasks/abc224_e


import sys
input = sys.stdin.buffer.readline

H, W, N = map(int, input().split())
mxr = [0] * H
mxc = [0] * W
ans = [0] * N
mp = dict()
r, c, a = [0]*N, [0]*N, [0]*N
for i in range(N):
    r[i], c[i], a[i] = map(int, input().split())
    r[i] -= 1
    c[i] -= 1
    if a[i] in mp:
        mp[a[i]].append(i)
    else:
        mp[a[i]] = [i]

for k, ilist in sorted(mp.items(), reverse=True):
    for i in ilist:
        ans[i] = max(mxr[r[i]], mxc[c[i]])
    for i in ilist:
        mxr[r[i]] = max(mxr[r[i]], ans[i] + 1)
        mxc[c[i]] = max(mxc[c[i]], ans[i] + 1)

for i in range(N):
    print(ans[i])




# # 1 WA
# import sys
# input = sys.stdin.buffer.readline
# INF = 1001001001

# H, W, N = map(int, input().split())
# koma = []
# yoko = [[INF, -1] for _ in range(H)]
# tate = [[INF, -1] for _ in range(W)]
# for i in range(N):
#     r, c, a = map(int, input().split())
#     koma.append([a, r-1, c-1, i, 0])
# koma.sort(reverse=True)
# # print(koma)

# for i in range(N):
#     a, r, c, _, now = koma[i]
#     # print(a, r, c, i, now, koma[i])
#     if yoko[r][0]>a:
#         now = max(now, yoko[r][1]+1)
#     elif yoko[r][0]==a:
#         now = max(now, yoko[r][1])
#     if tate[c][0]>a:
#         now = max(now, tate[c][1]+1)
#     elif tate[c][0]==a:
#         now = max(now, tate[c][1])
#     yoko[r][0] = a
#     yoko[r][1] = now
#     tate[c][0] = a
#     tate[c][1] = now
#     koma[i][4] = now
#     # print(a, r, c, i, now, koma[i])
# # print(koma)
# # print(yoko)
# # print(tate)

# idx = [-1] * N
# for i in range(N):
#     idx[koma[i][3]] = i
# # print(idx)

# for i in range(N):
#     print(koma[idx[i]][4])


