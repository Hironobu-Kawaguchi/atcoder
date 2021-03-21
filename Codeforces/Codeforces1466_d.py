# https://codeforces.com/contest/1466/problem/D

# import sys
# sys.setrecursionlimit(10 ** 7)
# import copy

def main():
    n = int(input())
    w = list(map(int, input().split()))
    edge = [[] for _ in range(n)]
    for i in range(n-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)
    weights = []
    for i in range(n):
        if len(edge[i])>=2:
            for _ in range(len(edge[i]) - 1):
                weights.append(w[i])
    weights.sort(reverse=True)
    ans = [sum(w)]
    for k in range(n-1):
        if k>0:
            ans.append(ans[-1] + weights[k-1])
    print(*ans)
    return

t = int(input())
for i in range(t):
    main()
