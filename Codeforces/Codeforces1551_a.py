# http://codeforces.com/contest/1551/problem/A


def main():
    n = int(input())
    div, mod = divmod(n, 3)
    c1 = div
    c2 = div
    if mod==2:
        c2 += 1
    elif mod==1:
        c1 += 1
    print(c1, c2)
    return

t = int(input())
for i in range(t):
    main()
