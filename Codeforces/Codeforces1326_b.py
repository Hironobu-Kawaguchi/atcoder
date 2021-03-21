# https://codeforces.com/contest/1326/problem/B

def main():
    n = int(input())
    b = list(map(int, input().split()))
    x = [0]
    a = []
    maxa = 0
    for i in range(n):
        a.append(b[i]+x[i])
        maxa = max(maxa, a[i])
        x.append(maxa)
    print(*a)

main()
