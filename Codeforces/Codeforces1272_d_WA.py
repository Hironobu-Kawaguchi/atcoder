# https://codeforces.com/contest/1272/problem/D

n = int(input())
a = list(map(int, input().split()))

ans = 0
cnt1 = 1
cnt2 = 0
for i in range(n-1):
    if a[i] < a[i+1]:
        cnt1 += 1
    else:
        ans = max(ans, cnt1)
        if cnt2 != 0 and (a[i-cnt1] > a[i-cnt1-2] or a[i-cnt1+1] > a[i-cnt1-1]):
            ans = max(ans, cnt1 + cnt2 - 1)
        cnt2 = cnt1
        cnt1 = 1
ans = max(ans, cnt1)
if cnt2 != 0 and (a[n-cnt1] > a[n-cnt1-2] or (cnt1 > 1 and a[n-cnt1+1] > a[n-cnt1-1])):
    ans = max(ans, cnt1 + cnt2 - 1)

print(ans)
