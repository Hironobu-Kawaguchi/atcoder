# https://codeforces.com/contest/1481/problem/D
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    G = [input().strip() for _ in range(n)]
    if m%2:
        ans = [1,2] * ((m+1)//2)
        print("YES")
        print(*ans)
        return
    for i in range(n):
        for j in range(n):
            if i==j: continue
            if G[i][j] == G[j][i]:
                ans = [i+1, j+1] * (m//2) + [i+1]
                print("YES")
                print(*ans)
                return
    for i in range(n):
        for j in range(n-1):
            if i==j: continue
            if G[i][j] != G[i][j+1]:
                b = 0
                while b==i or b==j or b==j+1:
                    b += 1
                    if b>=n:
                        print('NO')
                        return
                if G[b][i] == G[i][j]:
                    c, d = i+1, j+1
                else:
                    c, d = i+1, j+2
                b += 1
                a = 1
                while a==b or a==c or a==d:
                    a += 1
                    if a>n:
                        print('NO')
                        return
                e = 1
                while e==a or e==b or e==c or e==d:
                    e += 1
                    if e>n:
                        print('NO')
                        return
                if (m//2)%2:
                    ans = [b] + [a, b] * (m//2//2) + [c] + [d, e] * (m//2//2) + [d]
                else:
                    ans =       [a, b] * (m//2//2) + [c] + [d, e] * (m//2//2)
                print("YES")
                print(*ans)
                return
    print('NO')
    return

t = int(input())
for i in range(t):
    main()
