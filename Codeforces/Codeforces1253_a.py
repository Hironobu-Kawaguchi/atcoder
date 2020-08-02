# https://codeforces.com/contest/1253/problem/A
# Codeforces Round #600 (Div. 2)

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = "YES"
    flg = 0
    for j in range(n):
        if a[j] == b[j] and flg == 0:
            continue
        elif flg == 0:
            diff = b[j] - a[j]
            flg = 1
        elif b[j] - a[j] == diff and flg == 1:
            continue
        elif a[j] == b[j] and flg == 1:
            flg = 2
        elif a[j] == b[j] and flg == 2:
            continue
        else:
            ans = "NO"
    if diff < 0:
        ans = "NO"
    print(ans)
