# https://codeforces.com/contest/1481/problem/B

# import sys
# sys.setrecursionlimit(10 ** 7)
# import copy

def main():
    n, k = map(int, input().split())
    k = min(k, 100*n)
    h = list(map(int, input().split()))
    h.append(0)
    ans = -1
    for _ in range(k-1):
        for i in range(n):
            if h[i]<h[i+1]:
                h[i] += 1
                break
    else:
        for i in range(n):
            if h[i]<h[i+1]:
                h[i] += 1
                ans = i+1
                break
    print(ans)
    return

t = int(input())
for i in range(t):
    main()
