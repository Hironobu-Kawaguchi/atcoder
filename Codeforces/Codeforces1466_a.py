# https://codeforces.com/contest/1466/problem/A

# import sys
# sys.setrecursionlimit(10 ** 7)
# import copy

def main():
    n = int(input())
    x = list(map(int, input().split()))
    s = set()
    for i in range(n):
        for j in range(n):
            if x[i]!=x[j]:
                s.add(abs(x[i]-x[j]))
    # print(s)
    print(len(s))
    return

t = int(input())
for i in range(t):
    main()
