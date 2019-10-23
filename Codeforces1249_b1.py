# https://codeforces.com/contest/1249/problem/B1
# Codeforces Round #595 (Div. 3)

q = int(input())
for i in range(q):
    n = int(input())
    p = list(map(int, input().split()))
    tmp = p.copy()
    ans = [0] * n
    cnt = 1
    while 0 in ans:
        for j in range(n):
            if ans[j] != 0:
                continue
            tmp[j] = p[tmp[j]-1]
            if tmp[j] == p[j]:
                ans[j] = cnt
        cnt += 1
    print(*ans)
