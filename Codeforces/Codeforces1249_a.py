# https://codeforces.com/contest/1249/problem/A
# Codeforces Round #595 (Div. 3)

q = int(input())
for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    for j in range(n-1):
        for k in range(j+1, n):
            if abs(a[j] - a[k]) == 1:
                ans = 2
    print(ans)
