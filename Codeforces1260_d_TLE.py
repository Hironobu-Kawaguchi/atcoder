# https://codeforces.com/contest/1260/problem/D

m, n, k, t = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

dlr = []
for i in range(k):
    _l, _r, _d = map(int, input().split())
    dlr.append((_d, _l, _r))
dlr.sort(reverse=True)
# print(dlr)

# 二分探索
al = 0
ar = m

def chk(a):
    global dlr
    mnl = n
    mxr = 0
    needtime = n + 1
    for i in range(k):
        if dlr[i][0] <= a:
            break
        else:
            mnl = min(mnl, dlr[i][1])
            mxr = max(mxr, dlr[i][2])
            needtime = n + 1 + 2 * (mxr - mnl + 1)
    if needtime > t:
        return False
    else:
        return True

while ar > al + 1:
    i = (al + ar) // 2
    if chk(a[i]):
        ar = i
    else:
        al = i
if al == 0:
    if chk(a[0]):
        ar = 0

ans = m - ar
print(ans)
