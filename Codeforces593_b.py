# https://codeforces.com/contest/1236/problem/C

n = int(input())
ans = [[] for _ in range(n)]

for i in range(n**2):
    j = i % (n*2)
    if j >= n:
        j = 2*n - j -1
    ans[j].append(i+1)

for i in range(n):
    print(*ans[i])