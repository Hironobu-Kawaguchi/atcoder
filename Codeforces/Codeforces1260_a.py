# https://codeforces.com/contest/1260/problem/0

n = int(input())
for i in range(n):
    c, sumi = map(int, input().split())
    ans = 0
    while sumi > 0:
        tmp = (sumi + c - 1) // c
        ans += tmp*tmp
        sumi -= tmp
        c -= 1
    print(ans)
