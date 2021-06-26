# https://atcoder.jp/contests/ABC207/tasks/abc207_c

n = int(input())
lr = []
for i in range(n):
    t, l, r = map(int, input().split())
    if t==1:
        lr.append((l,r))
    elif t==2:
        lr.append((l,r-0.5))
    elif t==3:
        lr.append((l+0.5,r))
    else:
        lr.append((l+0.5,r-0.5))
ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        if lr[i][0]>lr[j][1] or lr[j][0]>lr[i][1]: continue
        ans += 1
        # print(i, j)

print(ans)
