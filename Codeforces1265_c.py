# https://codeforces.com/contest/1265/problem/C

def main():
    n = int(input())
    p = list(map(int, input().split()))
    mx = n//2
    while mx != 0 and p[mx] == p[mx-1]:
        mx -= 1
    g, s, b = 0, 0, 0

    for i in range(mx):
        g += 1
        if p[i] != p[i+1]:
            break
    if g == mx:
        return [0, 0, 0]

    for i in range(g, mx):
        s += 1
        if p[i] != p[i+1] and g < s:
            break
    if g+s == mx:
        return [0, 0, 0]

    b = mx - g - s
    if g >= b:
        return [0, 0, 0]
    
    return [g, s, b]


t = int(input())
for i in range(t):
    print(*main())
