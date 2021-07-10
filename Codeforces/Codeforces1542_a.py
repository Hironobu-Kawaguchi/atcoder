# https://codeforces.com/contest/1542/problem/A

def main():
    n = int(input())
    a = list(map(int, (input().split())))
    odds = 0
    for i in range(2*n):
        if a[i]%2==1:
            odds += 1
    if odds==n:
        print("Yes")
    else:
        print("No")
    return


t = int(input())
for _ in range(t):
    main()

