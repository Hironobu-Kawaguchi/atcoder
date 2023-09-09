# https://atcoder.jp/contests/abc319/tasks/abc319_d

INF = 1001001001001001001
N, M = map(int, input().split())
L = list(map(int, input().split()))

# sum_len = -1
max_len = 0
for i in range(N):
    # sum_len += L[i] + 1
    max_len = max(max_len, L[i])

l, r = max_len, INF
# l, r = 0, INF

def ok(w):
    cnt = 0
    cur = 0
    for i in range(N):
        if cur + L[i] + 1 > w + 1:
            cnt += 1
            cur = 0
        cur += L[i] + 1
    return cnt < M

while r-l > 1:
    w = (l+r)//2
    if ok(w):
        r = w
    else:
        l = w

# print(l, r)
if ok(l):
    print(l)
else:
    print(r)
