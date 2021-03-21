# https://codeforces.com/contest/1248/problem/A
# Codeforces Round #594 (Div. 2)

t = int(input())
for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    podd = 0
    peven = 0
    for j in range(n):
        if p[j] % 2:
            podd += 1
        else:
            peven += 1
    m = int(input())
    q = list(map(int, input().split()))
    qodd = 0
    qeven = 0
    for j in range(m):
        if q[j] % 2:
            qodd += 1
        else:
            qeven += 1
    print(podd*qodd + peven*qeven)
