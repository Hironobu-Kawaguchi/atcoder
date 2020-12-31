# https://codeforces.com/contest/1466/problem/B

# import sys
# sys.setrecursionlimit(10 ** 7)
# import copy

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    s = set()
    for i in range(n):
        if i==0:
            now = x[i]
        else:
            if x[i]==now:
                now = x[i]+1
            elif x[i]>now:
                now = x[i]
        s.add(now)
    # print(s)
    print(len(s))
    return

t = int(input())
for i in range(t):
    main()
