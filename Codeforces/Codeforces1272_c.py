# https://codeforces.com/contest/1272/problem/C

n, k = map(int, input().split())
s = input()
c = set(input().split())

ans = 0
cnt = 0
for i in range(n):
    if s[i] in c:
        cnt += 1
    elif cnt > 0:
        ans += cnt*(cnt+1)//2
        cnt = 0
ans += cnt*(cnt+1)//2

print(ans)
