# https://codeforces.com/contest/1355/problem/A

def main():
    a, k = map(int, input().split())
    for _ in range(k-1):
        lsta = list(map(int, list(str(a))))
        if min(lsta)==0 : break
        a += max(lsta) * min(lsta)
    return a

t = int(input())
for i in range(t):
    print(main())

