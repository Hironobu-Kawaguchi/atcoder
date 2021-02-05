# https://codeforces.com/contest/1481/problem/C

# import sys
# sys.setrecursionlimit(10 ** 7)
# import copy

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    q = [[] for _ in range(n+1)]
    idx = [-1] * (n+1)
    for i in range(n):
        idx[b[i]] = i+1
        if a[i]!=b[i]:
            q[b[i]].append(i+1)
    x = [0]*m
    ok = -1
    for j in range(m-1, -1, -1):
        # for i in range(n):
        #     if a[i]!=b[i] and b[i]==c[j]:
        #         x[j] = i+1
        #         a[i] = b[i]
        #         ok = i+1
        #         break
        if q[c[j]]:
            x[j] = q[c[j]].pop()
            ok = x[j]
        elif ok!=-1:
            x[j] = ok
        elif idx[c[j]]!=-1:
            x[j] = idx[c[j]]
            ok = x[j]
        else:
            print('NO')
            return
    for i in range(n+1):
        if q[i]:
            print('NO')
            return
    print('YES')
    print(*x)
    return

t = int(input())
for i in range(t):
    main()
